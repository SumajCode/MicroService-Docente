from src.infra.db.conn import Conexion
from src.config.conf import BaseConf
from src.infra.db.Table import Tabla

class Ejecutar:
    def __init__(self):
        """
        Initializes the Ejecutar class by connecting to the database.
        If POSTGRES_ACTIVE is True, it connects to the PostgreSQL database.
        If SQL_ACTIVE is True, it connects to the SQL Server database.
        If both are True, it connects to both databases.
        """
        connexion = Conexion()
        if BaseConf.POSTGRES_ACTIVE:
            self.connPostSQL = connexion.conectarPostgres()
            self.connSQL = None
        if BaseConf.SQL_ACTIVE:
            self.connSQL = connexion.conectarSQL()
            self.connPostSQL = None
        # if BaseConf.POSTGRES_ACTIVE and BaseConf.SQL_ACTIVE:
        #     self.connPostSQL = Conexion.conectarPostgres()
        #     self.conn2 = Conexion.conectarSQL()

    def ejecutarConsulta(self, consulta: str):
        # if BaseConf.POSTGRES_ACTIVE and BaseConf.SQL_ACTIVE:
        #     self.connPostSQL.execute(consulta)
        #     self.conn2.execute(consulta)
        """
        Executes a SQL query on the database and returns the results.

        This function takes a SQL query, executes it on the database, and returns the
        results of the query as a list of tuples.

        Args:
            consulta (str): The SQL query to be executed.

        Returns:
            list: A list of tuples containing the results of the query.
        """
        conn = self.connSQL if self.connPostSQL is None else self.connPostSQL
        conn.execute(consulta)
        conn.connection.commit()
        return conn.fetchall()

    def crearTabla(self):
        def nuevaMigracion(model: Tabla):
            """
            Creates a new table in the database if it does not already exist.

            This function takes a model class, instantiates it, and checks if the table
            represented by the model exists in the database. If the table does not exist,
            it executes the SQL command to create the table. If the table already exists,
            it notifies the user.

            Args:
                model (Tabla): A class representing the table to be created.

            Returns:
                str: A message indicating whether the table was successfully created or
                    if it already exists.
            """

            modelo = model()
            print("En espera de la creacion de la tabla...")
            consulta = self.ejecutarConsulta(f"SHOW FULL TABLES FROM {BaseConf.SQL_DB}")
            nombreColumna = f'Tables_in_{BaseConf.SQL_DB}'
            if modelo.nombreTabla not in [tabla[nombreColumna] for tabla in consulta]:
                self.ejecutarConsulta(modelo.consultaCrearTabla())
                print(f"Creacion de tabla {modelo.nombreTabla} exitosa.")
                return f"Creacion de tabla exitosa."
            else:
                self.actualizarTabla(model)
            print(f"La tabla {modelo.nombreTabla} ya existe.")
            return f"La tabla ya existe."
        return nuevaMigracion
    
    def eliminarTablas(self):
        pass

    def actualizarTabla(self, modelo: Tabla):
        consulta = f"DESCRIBE {modelo.nombreTabla};"
        