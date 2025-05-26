import pymysql
import pymysql.cursors
import psycopg

from src.config.conf import BaseConf

class Conexion:
    def conectarSQL(self):
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
            cursorclass=pymysql.cursors.DictCursor)
        return conn.cursor()

    def conectarPostgres(self):
        """Connect to a PostgreSQL database
        
        Parameters
        ----------
        None
        
        Returns
        -------
        psycopg2.extensions.cursor
            A cursor for the database connection
        """
        connextion = f"dbname={BaseConf.POSTGRES_DB}"
        connextion += f" username={BaseConf.POSTGRES_USER}"
        connextion += f" password={BaseConf.POSTGRES_PASSWORD}"
        with psycopg.connect(connextion) as conn:
            with conn.cursor() as cur:
                return cur
