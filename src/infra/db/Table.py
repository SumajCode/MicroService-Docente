from .Column import Columna
from .Query import *

class Tabla:
    def __init__(self, nombreTabla: str, columnas: list):
        self.nombreTabla = nombreTabla
        self.columnas = columnas

    def consultaCrearTabla(self):
        valores = []
        for i in self.columnas:
            valores.append(i.columnaSQL())
        return f"""
CREATE TABLE {self.nombreTabla} (
    {",\n".join(valores)}
    {foreignKey(self.columnas)}
    {index(self.columnas, self.nombreTabla) if BaseConf.SQL_ACTIVE else ""});
{index(self.columnas, self.nombreTabla) if BaseConf.POSTGRES_ACTIVE else ""}"""
    
    def getColumnas(self):
        return self.columnas