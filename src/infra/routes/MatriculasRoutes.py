from flask import Blueprint
from flask import request

from src.infra.controllers.MatriculaController import MatriculaController

controlador = MatriculaController()
blueprint = Blueprint('matricula', __name__, url_prefix='/matricula')

@blueprint.route('/eliminar', methods=['DELETE'])
def eliminarMatricula():
    return controlador.eliminar(request)

@blueprint.route('/eliminar/todo', methods=['DELETE'])
def eliminarMatriculas():
    return controlador.eliminarTodo(request)

@blueprint.route('/materia', methods=['GET'])
def obtenerMatriculaPorMateria():
    return controlador.listarMatriculadosPorMateria(request)

@blueprint.route('/listar', methods=['GET'])
def obtenerMatriculas():
    return controlador.listar(request)

@blueprint.route('/crear', methods=['POST'])
def crearMatricula():
    return controlador.crear(request)

@blueprint.route('/crear/matriculas', methods=['POST'])
def crearMatriculas():
    return controlador.crearPorArchivo(request)

@blueprint.route('/editar', methods=['PATCH'])
def editarMatricula():
    return controlador.modificar(request)