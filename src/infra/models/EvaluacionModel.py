from src.infra.db.Table import Tabla
from src.infra.db.Column import Columna
from src.infra.db.DataType import *

class EvaluacionModel(Tabla):
    nombreTabla='evaluacion'
    columnas=[
        Columna(
            nombreColumna='id', 
            tipoColumna=Integer(), 
            llavePrimaria=True, 
            autoIncremental=True),
        Columna(
            nombreColumna='fecha_evaluacion', 
            tipoColumna=DateTime()),
        Columna(
            nombreColumna='calificacion',
            tipoColumna=Decimal(4, 2)),
        Columna(
            nombreColumna='tipo_evaluacion',
            tipoColumna=String()),
        Columna(
            nombreColumna='id_materia_eval',
            tipoColumna=Integer(),
            llaveForanea=True,
            referenciaTabla='materia'),
        Columna(
            nombreColumna='id_estudiante',
            tipoColumna=Integer())]
    
    def __init__(self):
        super().__init__(self.nombreTabla, self.columnas)

