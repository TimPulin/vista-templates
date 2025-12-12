import pymysql
from queries import GET_ALL_TEMPLATES_QUERY


DB_PARAMS = {
    'host': '192.168.1.3',
    'port': 2401,
    'user': 'dbuser',
    'password': 'dbpassword',
    'database': 's11'
}


def connect_db(connection_params):
    connection = pymysql.connect(**connection_params)
    return connection


def close_db(connection):
    cursor = connection.cursor()
    cursor.close()


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print('ошибка выполнения запроса', e)
    finally:
        cursor.close()


def get_all_templates(connection):
    return execute_query(connection, GET_ALL_TEMPLATES_QUERY)


def start_testing()
    connection = connect_db(DB_PARAMS)
    all_templates = execute_query(connection, GET_ALL_TEMPLATES_QUERY)