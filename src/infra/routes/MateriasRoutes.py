from flask import Blueprint
from flask import request

from infra.controllers.MateriaController import MateriaController

controlador = MateriaController()
blueprint = Blueprint('materia', __name__, url_prefix='/materia')

@blueprint.route('/eliminar', methods=['DELETE'])
def eliminarMateria():
    return controlador.eliminar(request)

@blueprint.route('/eliminar/todo', methods=['DELETE'])
def eliminarMaterias():
    return controlador.eliminarTodo(request)

@blueprint.route('/listar', methods=['GET'])
def obtenerMaterias():
    return controlador.listar()

@blueprint.route('/docentes', methods=['GET'])
def obtenerDocentesPorMateria():
    return controlador.listarPorDocente(request)

@blueprint.route('/crear', methods=['POST'])
def crearMateria():
    return controlador.crear(request)

@blueprint.route('/editar', methods=['PATCH'])
def editarMateria():
    return controlador.modificar(request)