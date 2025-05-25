import pymysql
import pymysql.cursors
import psycopg

from ...config.conf import BaseConf

class Conexion:
    def conectarSQL():
        """
        Connect to a SQLite database and return a cursor object.

        This function establishes a connection to the SQLite database specified
        in the configuration and returns a cursor object to execute SQL queries.

        Parameters
        ----------
        None

        Returns
        -------
        sqlite3.Cursor
            A cursor object for executing SQL queries on the database.
        """

        conn = pymysql.connect(
            host=BaseConf.SQL_HOST, 
            user=BaseConf.SQL_USER, 
            passwd=BaseConf.SQL_PASSWORD, 
            db=BaseConf.SQL_DB,
            cursorclass=pymysql.cursors.DictCursor
            )
        return conn.cursor()

    def conectarPostgres():
        """Connect to a PostgreSQL database
        
        Parameters
        ----------
        None
        
        Returns
        -------
        psycopg2.extensions.cursor
            A cursor for the database connection
        """
        with psycopg.connect(f"dbname={BaseConf.POSTGRES_DB} username={BaseConf.POSTGRES_USER} password={BaseConf.POSTGRES_PASSWORD}") as conn:
            with conn.cursor() as cur:
                return cur
