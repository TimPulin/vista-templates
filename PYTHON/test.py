import pymysql
from test2 import region_list

SCHEMA_NAME = 's11'


def connect_db(schema_name):
    connection = pymysql.connect(
        host='10.162.109.254',
        port=3306,
        user='dbuser',
        password='dbpassword',
        database=schema_name
    )
    return connection


def close_db(connection):
    cursor = connection.cursor()
    cursor.close()


def format_query(schema_name, query):
    return """
    INSERT INTO {schema_name}.rbRegion_2025 (code, name) 
    VALUES ('{code}', '{name}');
    """.format(schema_name=schema_name, code=query['code'], name=query['name'])


def execute_query(connection, query_list):
    try:
        with connection.cursor() as loc_cursor:
            for query in query_list:
                loc_cursor.execute(query)
        connection.commit()
        print('запросы выполнен')
    except Exception as e:
        print('провален запрос', e)
        connection.rollback()


if __name__ == '__main__':
    conn = connect_db(SCHEMA_NAME)
    print('начало работы')
    for item in region_list:
        new_query = format_query(SCHEMA_NAME, item)
        execute_query(conn, [new_query])

    close_db(conn)
    print('работа с БД завершена')
