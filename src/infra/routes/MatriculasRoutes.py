from flask_openapi.blueprint import APIBlueprint
from flask_openapi.models.tag import Tag
from flask import request

from infra.controllers.MatriculaController import MatriculaController

controlador = MatriculaController()
tag = Tag(name='Matricula', description='Formas de matricular a un estudiante')
blueprint = APIBlueprint(
    'matricula',
    __name__,
    abp_tags=[tag],
    url_prefix='/matriculas')

@blueprint.delete('/', tags=[tag])
def eliminarMatricula():
    return controlador.eliminar(request)

@blueprint.get('/materia', tags=[tag])
def obtenerMatriculaPorMateria():
    return controlador.listar(request)

@blueprint.post('/', tags=[tag])
def crearMatricula():
    return controlador.crear(request)

@blueprint.post('/matriculas', tags=[tag])
def crearMatriculas():
    return controlador.crearMatriculados(request)

@blueprint.post('/matricula/id', tags=[tag])
def crearMatriculasPorIdMateria():
    return controlador.crearPorIDMateria(request)

@blueprint.get('/estudiante', tags=[tag])
def listarMatriculasPorIdEstudiante():
    return controlador.listarMatriculadoId(request)