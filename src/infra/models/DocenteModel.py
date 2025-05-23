from ..db.Column import Columna
from ..db.Table import Tabla
from ..db.DataType import *

class DocenteModel(Tabla):
    nombreTabla='docente'
    columnas=[
        Columna(
            nombreColumna='id', 
            tipoColumna=Integer(),
            llavePrimaria = True,
            autoIncremental = True,
            indexado=True),
        Columna(
            nombreColumna='id_persona',
            referenciaTabla='persona',
            tipoColumna=Integer(),
            indexado=True)]

    def __init__(self):
        super().__init__(self.nombreTabla, self.columnas)