from flask import request
from flask_openapi.models.tag import Tag
from flask_openapi.blueprint import APIBlueprint

from infra.controllers.MateriaController import MateriaController

controlador = MateriaController()
tag = Tag(name='Materias', description='Formas de agregar, retirar, leer y modificar materias')
blueprint = APIBlueprint('materias', __name__, abp_tags=[tag], url_prefix='/materias')

@blueprint.delete('/')
def eliminarMateria():
    return controlador.eliminar(request)

@blueprint.delete('/all')
def eliminarMaterias():
    return controlador.eliminarTodo(request)

@blueprint.get('/')
def obtenerMaterias():
    return controlador.listar()

@blueprint.get('/id')
def obtenerMateriaId():
    return controlador.listarId(request)

@blueprint.get('/docentes')
def obtenerDocentesPorMateria():
    return controlador.listarPorDocente(request)

@blueprint.post('/')
def crearMateria():
    return controlador.crear(request)

@blueprint.patch('/')
def editarMateria():
    return controlador.modificar(request)