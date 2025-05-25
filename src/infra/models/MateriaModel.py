from ..db.Table import Tabla
from ..db.Column import Columna
from ..db.DataType import *


class MateriaModel(Tabla):
    nombreTabla='materia',
    columnas=[
        Columna(
            nombreColumna='id', 
            tipoColumna=Integer(), 
            llavePrimaria=True, 
            autoIncremental=True),
        Columna(
            nombreColumna='nombre_materia', 
            tipoColumna=String()),
        Columna(
            nombreColumna='nivel_estudio',
            tipoColumna=String()),
        Columna(
            nombreColumna='id_docente',
            tipoColumna=Integer(),
            llaveForanea=True,
            referenciaTabla='docente')
    ]
    
    def __init__(self):
        super().__init__(self.nombreTabla, self.columnas)

