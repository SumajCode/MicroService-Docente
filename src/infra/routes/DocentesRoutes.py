from flask import Blueprint
from flask import request

from infra.controllers.DocenteController import DocenteController

controlador = DocenteController()
blueprint = Blueprint('docente', __name__, url_prefix='/docente')

@blueprint.route('/eliminar', methods=['DELETE'])
def eliminarDocente():
    return controlador.eliminar(request)

@blueprint.route('/eliminar/todo', methods=['DELETE'])
def eliminarDocentes():
    return controlador.eliminarTodo(request)

@blueprint.route('/listar', methods=['GET'])
def obtenerDocentes():
    return controlador.listar()

@blueprint.route('/materias', methods=['GET'])
def obtenerMateriasPorDocente():
    return controlador.listarMateriasPorDocente(request)

@blueprint.route('/crear', methods=['POST'])
def crearDocente():
    return controlador.crear(request)

@blueprint.route('/editar', methods=['PATCH'])
def editarDocente():
    return controlador.modificar(request)