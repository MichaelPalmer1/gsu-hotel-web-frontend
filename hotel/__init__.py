from flask import request
from flask.ext.api import FlaskAPI
from flask.ext.mysqldb import MySQL
from collections import OrderedDict
from _mysql_exceptions import MySQLError

app = FlaskAPI(__name__)
mysql = MySQL(app)


@app.route("/", methods=['GET'])
def index():
    result = {}
    conn = mysql.connect()
    cursor = conn.cursor()

    query_type = request.args.get('type', 'SELECT').upper()
    query = request.args.get('query', None)

    if query:
        try:
            cursor.execute(query)
            if query_type == 'SELECT':
                data = cursor.fetchall()
                if data:
                    fields = [i[0] for i in cursor.description]

                    result['data'] = []
                    for i, row in enumerate(data):
                        result['data'].append(OrderedDict())
                        for j, value in enumerate(row):
                            column = fields[j]
                            result['data'][i][column] = value
                else:
                    result['error'] = 'Data error'
        except MySQLError as e:
            result['error_code'] = e[0]
            result['error'] = e[1]
    else:
        result['error'] = 'No query provided'

    return result
