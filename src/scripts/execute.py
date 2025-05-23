from ..infra.db.conn import Conexion
from ..config.conf import BaseConf
from ..infra.db.Table import Tabla

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
        def nuevaMigracion(model: Tabla):
            modelo = model()
            print("En espera de la creacion de la tabla...")
            if modelo.nombreTabla not in [tabla[f'Tables_in_{BaseConf.SQL_DB}'] for tabla in self.ejecutarConsulta(f"SHOW FULL TABLES FROM {BaseConf.SQL_DB}")]:
                self.ejecutarConsulta(modelo.consultaCrearTabla())
                print("Creacion de tabla exitosa.")
                return "Creacion de tabla exitosa."
            print(f"La tabla {modelo.nombreTabla} ya existe.")
            return f"La tabla {modelo.nombreTabla} ya existe."
        return nuevaMigracion