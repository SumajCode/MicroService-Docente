from src.infra.db.Table import Tabla
from src.infra.db.Column import Columna
from src.infra.db.DataType import *
from src.infra.models.MateriaModel import MateriaModel
from src.infra.models.EvaluacionModel import EvaluacionModel
from src.infra.models.MatriculaModel import MatriculaModel
from src.infra.models.DocenteModel import DocenteModel

def test_query_table():
    tabla = Tabla(
        nombreTabla="test",
        columnas=[Columna("id", Integer(), llavePrimaria=True, autoIncremental=True),
        Columna("name", String()),
        Columna("email", String())]
    )
    print(tabla.consultaCrearTabla())

def test_query_materia():
    print(MateriaModel().consultaCrearTabla())

def test_query_evaluacion():
    print(EvaluacionModel().consultaCrearTabla())

def test_query_matricula():
    print(MatriculaModel().consultaCrearTabla())

def test_query_docente():
    print(DocenteModel().consultaCrearTabla())

test_query_table()

test_query_docente()

test_query_evaluacion()

test_query_materia()

test_query_matricula()