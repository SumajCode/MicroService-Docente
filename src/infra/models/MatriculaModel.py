from ..db.Column import Columna
from ..db.Table import Tabla
from ..db.DataType import Integer

class MatriculaModel(Tabla):
    nombreTabla='matricula'
    columnas=[
        Columna(
            nombreColumna='id', 
            tipoColumna=Integer(),
            llavePrimaria=True,
            autoIncremental=True),
        Columna(
            nombreColumna='id_materia',
            tipoColumna=Integer(),
            llaveForanea=True,
            columnaTablaRelacion='materia'),
        Columna(
            nombreColumna='id_estudiante',
            tipoColumna=Integer(),
            llaveForanea=True,
            columnaTablaRelacion='estudiante')
    ]

    def __init__(self):
        super().__init__(self.nombreTabla, self.columnas)
