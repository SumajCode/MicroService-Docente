from infra.db.Column import Columna
from infra.db.Table import Tabla
from infra.db.DataType import Integer

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
            referenciaTabla='materia'),
        Columna(
            nombreColumna='id_estudiante',
            tipoColumna=Integer())
    ]

    def __init__(self):
        super().__init__(self.nombreTabla, self.columnas)
