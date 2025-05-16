from db.Column import Columna
from db.Table import Tabla
from db.DataType import *

class DocenteModel():
    Tabla(
        'docente',
        Columna(
            nombreColumna='id', 
            tipoColumna=Integer(),
            llavePrimaria = True,
            autoIncemental = True),
        Columna(
            nombreColumna='id_persona',
            tipoColumna=Integer(),
            llaveForanea = True)
    )