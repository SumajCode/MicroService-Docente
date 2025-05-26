from infra.db.Column import Columna
from infra.db.Table import Tabla
from infra.db.DataType import *

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
            nombreColumna='nombre',
            tipoColumna=String()),
        Columna(
            nombreColumna='apellidos',
            tipoColumna=String()),
        Columna(
            nombreColumna='celular',
            tipoColumna=Integer()),
        Columna(
            nombreColumna='correo',
            tipoColumna=String()),
        Columna(
            nombreColumna='nacimiento',
            tipoColumna=Date()),
        Columna(
            nombreColumna='usuario',
            tipoColumna=String()),
        Columna(
            nombreColumna='password',
            tipoColumna=String()),
        Columna(
            nombreColumna='create_at',
            tipoColumna=DateTime()),
        Columna(
            nombreColumna='update_at',
            tipoColumna=DateTime())
        ]

    def __init__(self):
        super().__init__(self.nombreTabla, self.columnas)