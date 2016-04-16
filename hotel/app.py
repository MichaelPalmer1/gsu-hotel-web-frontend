from flask import request, abort, url_for
from _mysql_exceptions import MySQLError

from .settings.base import mysql, app
from .api_utils import get_tables, get_data, render_query


# this can be changed to a search instead using POST to not worry about get params
@app.route("/query", methods=['POST'])
def query():
    """
    This endpoint will execute whatever sql query is sent to it. Aside from being a glaring security hole, this will
    allow us to basically run whatever query we want and have the server render it out for us.

    ***
    The search query should be sent in JSON format with the 'query' key holding the query string itself.
    The request should also have the following header:
        Content-Type: application/json
    ***

    :return: a list of dicts, with each dict representing one row of the returned query, each key being a column
        name, and each key value being a piece of data
    """
    result = {}

    cursor = mysql.connection.cursor()

    # get the data from the POST request
    query = request.json.get('query')

    if query:
        try:
            cursor.execute(query)
            result = render_query(cursor)

        except MySQLError as e:
            result['error_code'] = e[0]
            result['error'] = e[1]
    else:
        result['error'] = 'No query provided in request'

    return result


@app.route("/")
def index():
    result = {}
    cursor = mysql.connection.cursor()

    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor]
    cursor.close()

    # for each table, generate a url for that table's detail and add it to the result dict
    for table in tables:
        result[table] = url_for('table_detail_view', table=table, _external=True)

    return result


@app.route("/<table>/", methods=['GET'])
def table_detail_view(table):
    # if the desired table is not a table in the database, throw a 404 back at the user
    if table not in get_tables():
        abort(404)

    # the result should be the equivalent of 'select * from table'
    result = get_data(table)

    return result
