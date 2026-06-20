from flask import request
from flask_openapi.models.tag import Tag
from flask_openapi.blueprint import APIBlueprint

from infra.controllers.DocenteController import DocenteController
from features.controllers.validations.Docente import EliminarResponse, request_elimnar_docente

controlador = DocenteController()
tag = Tag(name='Docentes', description='Formas de registrar, eliminar modificar y leer a los docentes')
blueprint = APIBlueprint('docentes', __name__, abp_tags=[tag], url_prefix='/docentes')

@blueprint.delete(
    '',
    summary='Eliminar docente',
    description='Elimina al docente con el id que se encuentre en el request',
    tags=[tag],
    responses={
        200:EliminarResponse
    },
    request_body=request_elimnar_docente)
def eliminarDocente():
    return controlador.eliminar(request)

@blueprint.delete('/all', tags=[tag])
def eliminarDocentes():
    return controlador.eliminarTodo(request)

@blueprint.get('', tags=[tag])
def obtenerDocentes():
    return controlador.listar()

@blueprint.get('/id', tags=[tag])
def obtenerDocente():
    return controlador.listarId(request)

@blueprint.get('/materias', tags=[tag])
def obtenerMateriasPorDocente():
    return controlador.listarMaterias(request)

@blueprint.post('', tags=[tag])
def crearDocente():
    return controlador.crear(request)

@blueprint.post('/login', tags=[tag])
def loginDocente():
    return controlador.login(request)

@blueprint.patch('/', tags=[tag])
def editarDocente():
    return controlador.modificar(request)