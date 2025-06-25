from flask import Blueprint
from flask import request

from infra.controllers.MatriculaController import MatriculaController

controlador = MatriculaController()
blueprint = Blueprint('matricula', __name__, url_prefix='/matricula')

@blueprint.route('/eliminar', methods=['DELETE'])
def eliminarMatricula():
    return controlador.eliminar(request)

@blueprint.route('/listar/materia', methods=['GET'])
def obtenerMatriculaPorMateria():
    return controlador.listar(request)

@blueprint.route('/crear', methods=['POST'])
def crearMatricula():
    return controlador.crear(request)

@blueprint.route('/crear/matriculas', methods=['POST'])
def crearMatriculas():
    return controlador.crearMatriculados(request)

@blueprint.route('/crear/matricula/id', methods=['POST'])
def crearMatriculasPorIdMateria():
    return controlador.crearPorIDMateria(request)

@blueprint.route('/listar/estudiante', methods=['GET'])
def crearMatriculasPorIdEstudiante():
    return controlador.listarMatriculadoId(request)