from flask import request
from flask_openapi.models.tag import Tag
from flask_openapi.blueprint import APIBlueprint

from infra.controllers.MateriaController import MateriaController
from features.controllers.validations.Materia import (
    RegistrarResponse,
    request_registrar_mateira,
    request_modificar_mateira,
    EliminarResponse,
)

controlador = MateriaController()
tag = Tag(name='Materias', description='Formas de agregar, retirar, leer y modificar materias')
blueprint = APIBlueprint('materias', __name__, abp_tags=[tag], url_prefix='/materias')

@blueprint.delete(
    '/<int:id>',
    tags=[tag],
    summary='Eliminar materia',
    description='Eliminar materia mediante el id de la materia.',
    responses={
        200: EliminarResponse
    }
    )
def eliminarMateria():
    return controlador.eliminar(request)

@blueprint.delete(
    '/all',
    tags=[tag],
    summary='Eliminar todas las materias',
    description='Elimina todas las materias registradas.',
    responses={
        200: EliminarResponse
    }
    )
def eliminarMaterias():
    return controlador.eliminarTodo(request)

@blueprint.get(
    '',
    tags=[tag],
    summary='Obtener materias',
    description='Obtiene todas las materias registradas',
    responses={
        200: EliminarResponse
    }
    )
def obtenerMaterias():
    return controlador.listar()

@blueprint.get(
    '/<int:id>',
    tags=[tag],
    summary='Obtener unica materia',
    description='Obtener una materia desde el id',
    responses={
        200: EliminarResponse
    }
    )
def obtenerMateriaId():
    return controlador.listarId(request)

@blueprint.get(
    '/docentes/<int:id>',
    tags=[tag],
    summary='Obtener docentes por materia',
    description='Obtener los docentes que estan relacionados con la materia segun el id.',
    responses={
        200: EliminarResponse
    }
    )
def obtenerDocentesPorMateria():
    return controlador.listarPorDocente(request)

@blueprint.post(
    '',
    tags=[tag],
    summary='Registrar materia',
    responses={
        201: RegistrarResponse
    },
    request_body=request_registrar_mateira)
def crearMateria():
    return controlador.crear(request)

@blueprint.patch(
    '',
    tags=[tag],
    summary='Modificar materia',
    responses={
        200: EliminarResponse
    },
    request_body=request_modificar_mateira)
def editarMateria():
    return controlador.modificar(request)