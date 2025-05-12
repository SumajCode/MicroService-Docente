import Column

class Tabla:
    def __init__(self, nombreTabla: str, **columnas: Column):
        self.nombreTabla = nombreTabla
        self.columnas = columnas

    def consultaCrearTabla(self):
        values = [i.columnaSQL() for i in self.columnas]
        return f"CREATE TABLE {self.nombreTabla} ({",".join(values)})"