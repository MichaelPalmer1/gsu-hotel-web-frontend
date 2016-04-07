from .settings.base import mysql

def get_tables():
    """
    Get a list of table names
    :return: list of table names
    """
    cursor = mysql.connection.cursor()
    cursor.execute("SHOW TABLES")

    return [table[0] for table in cursor]

def get_data(table):
    """

    :param table:
    :return:
    """
    cursor = mysql.connection.cursor()
    cursor.execute("select * from %s" % table)

    return render_query(cursor)


def render_query(cursor):

    # the result will be a series of dicts in which each item is a serialized row from 'table'
    result_list = []

    # loop over all rows
    for item in cursor:
        result = {}
        # loop over all values in each row
        for i, field in enumerate(item):
            column_name = cursor.description[i][0]
            row_value = item[i]
            result[column_name] = row_value

        result_list.append(result)


    return result_list
