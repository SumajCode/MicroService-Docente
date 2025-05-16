from db.Column import Columna
from db.Table import Tabla
from db.DataType import *

class MatriculaModel():
    Tabla(
        'matricula',
        Columna(
            nombreColumna='id', 
            tipoColumna=Integer(),
            llavePrimaria = True,
            autoIncemental = True),
        Columna(
            nombreColumna='id_materia',
            tipoColumna=Integer(),
            llaveForanea = True,
            columnaTablaRelacion='materia',
            referennciaTablaID='id'),
        Columna(
            nombreColumna='id_estudiante',
            tipoColumna=Integer(),
            llaveForanea = True,
            columnaTablaRelacion='estudiante',
            referennciaTablaID='id')
    )