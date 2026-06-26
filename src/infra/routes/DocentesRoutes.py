from flask import request
from flask_openapi.models.tag import Tag
from flask_openapi.blueprint import APIBlueprint

from infra.controllers.DocenteController import DocenteController
from features.controllers.validations.Docente import (
    EliminarResponse,
    RegistrarResponse,
    request_registrar_docente,
    ModificarBody,
    request_modificar_docente
    )

controlador = DocenteController()
tag = Tag(name='Docentes', description='Formas de registrar, eliminar modificar y leer a los docentes')
blueprint = APIBlueprint('docentes', __name__, abp_tags=[tag], url_prefix='/docentes')

@blueprint.delete(
    '/<int:id>',
    summary='Eliminar docente',
    description='Elimina al docente con el id que se encuentre en el request',
    tags=[tag],
    responses={
        200:EliminarResponse
    })
def eliminarDocente():
    return controlador.eliminar(request)

@blueprint.delete(
    '/all',
    summary='Eliminar todos los docentes',
    description='Elimina a todos los docentes registrados',
    tags=[tag],
    responses={
        200:EliminarResponse
    })
def eliminarDocentes():
    return controlador.eliminarTodo(request)

@blueprint.get(
    '',
    summary='Obtener docentes',
    description='Obtiene todos los docentes registrados en una lista estructurada',
    tags=[tag],
    responses={
        200:EliminarResponse
    })
def obtenerDocentes():
    return controlador.listar()

@blueprint.get(
    '/<int:id>',
    summary='Obtener unico docente',
    description='Obtiene un docente por id en el request',
    tags=[tag],
    responses={
        200:EliminarResponse
    })
def obtenerDocente():
    return controlador.listarId(request)

@blueprint.get(
    '/materias',
    summary='Obtener materias por docente',
    description='Obtiene las materias de un docente segun su id',
    tags=[tag],
    responses={
        200:EliminarResponse
    })
def obtenerMateriasPorDocente():
    return controlador.listarMaterias(request)

@blueprint.post(
    '',
    summary='Crear docente',
    description='Registra a un docente a la vez mediante un formulario',
    tags=[tag],
    responses={
        201:RegistrarResponse
    },
    request_body=request_registrar_docente)
def crearDocente():
    return controlador.crear(request)

@blueprint.post(
    '/login',
    summary='Inicio de sesión',
    description='',
    tags=[tag],
    responses={
        200:EliminarResponse
    })
def loginDocente():
    return controlador.login(request)

@blueprint.patch(
    '/',
    summary='Editar docente',
    description='Edita el docente segun el id en el request',
    tags=[tag],
    responses={
        200:ModificarBody
    },
    request_body=request_modificar_docente)
def editarDocente():
    return controlador.modificar(request)