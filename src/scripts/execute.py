from ..infra.db.conn import Conexion
from ..config.conf import BaseConf

class Ejecutar:
    def __init__(self):
        if BaseConf.POSTGRES_ACTIVE:
            self.conn1 = Conexion.conectarPostgres()
            self.conn2 = None
        if BaseConf.SQL_ACTIVE:
            self.conn1 = Conexion.conectarSQL()
            self.conn2 = None
        # if BaseConf.POSTGRES_ACTIVE and BaseConf.SQL_ACTIVE:
        #     self.conn1 = Conexion.conectarPostgres()
        #     self.conn2 = Conexion.conectarSQL()
    
    def ejecutarConsulta(self, consulta: str):
        # if BaseConf.POSTGRES_ACTIVE and BaseConf.SQL_ACTIVE:
        #     self.conn1.execute(consulta)
        #     self.conn2.execute(consulta)
        self.conn1.execute(consulta)
        return self.conn1.fetchall()

    def crearTabla(self):
        def nuevaMigracion(query):
            print("En espera de la creacion de la tabla...")
            print(query())
            # if self.ejecutarConsulta(query):
            #     return "Creacion de tabla exitosa."
            # return "Error al crear la tabla."
        return nuevaMigracion