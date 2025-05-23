import pymysql
from ..config.conf import BaseConf

def crearBaseDatos():
    config = {
        'host': BaseConf.SQL_HOST,
        'user': BaseConf.SQL_USER,
        'password': BaseConf.SQL_PASSWORD,
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW DATABASES;")
            if BaseConf.SQL_DB not in [value['Database'] for value in cursor.fetchall()]:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {BaseConf.SQL_DB}")
                connection.commit()
                connection.close()
                return "Base de datos creada"
        connection.commit()
        connection.close()
        return "La base de datos ya existe."
    except Exception as e:
        return f"Error sql: {e}"

