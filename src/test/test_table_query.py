from orm.db.Table import Tabla
from orm.db.Column import Columna
from orm.db.DataType import *

def queryTable():
    tabla = Tabla(
        nombreTabla="test",
        columnas=[Columna("id", Integer(), llavePrimaria=True, autoIncremental=True),
        Columna("name", String()),
        Columna("email", String())]
    )
    print(tabla.consultaCrearTabla())

queryTable()