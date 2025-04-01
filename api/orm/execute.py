from conn import connect_sql, connect_postgres
from conf import BaseConf

class Execute:
    def __init__(self):
        if BaseConf.POSTGRES_ACTIVE:
            self.conn = connect_postgres()
        else:
            self.conn = connect_sql()
        pass
    
    def create_table(self, function):
        def new_migration():
            query = function()
            print("En espera de la creacion de la tabla...")
            if self.conn.execute(query):
                return "Creacion de tabla exitosa."
            return "Error al crear la tabla."
        
    def create_tables(self, function):
        def new_migrations():
            
            pass