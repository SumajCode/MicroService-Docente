from conn import connect_sql, connect_postgres
from api.src.config.conf import BaseConf

class Ejecutar:
    def __init__(self):
        if BaseConf.POSTGRES_ACTIVE:
            self.conn = connect_postgres()
        else:
            self.conn = connect_sql()
        pass
    
    def crearTabla(self, function):
        def nuevaMigracion():
            query = function()
            print("En espera de la creacion de la tabla...")
            if self.conn.execute(query):
                return "Creacion de tabla exitosa."
            return "Error al crear la tabla."
        
    def crearTablas(self, function):
        def nuevaMigracion():
            
            pass