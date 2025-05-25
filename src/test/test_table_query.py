from infra.db.Table import Tabla
from infra.db.Column import Columna
from infra.db.DataType import *

def test_query_table():
    tabla = Tabla(
        nombreTabla="test",
        columnas=[Columna("id", Integer(), llavePrimaria=True, autoIncremental=True),
        Columna("name", String()),
        Columna("email", String())]
    )
    print(tabla.consultaCrearTabla())

test_query_table()