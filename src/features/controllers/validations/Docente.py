from pydantic import BaseModel, Field
from flask_openapi.openapi import RequestBody
from flask_openapi.utils import get_model_schema
from features.controllers.validations.ResponseMain import Response

class EliminarBody(BaseModel):
    id: int = Field(examples=[1], description='Id del docente a eliminar')

class RegistrarBody(BaseModel):
    nombre: str = Field(examples=['Juan'], description='')
    apellidos: str = Field(examples=['Perez'], description='')
    celular: int = Field(examples=[76543210], description='')
    correo: str = Field(examples=['juan@perez.com'], description='')
    nacimiento: str = Field(examples=['01/01/2026'], description='')
    usuario: str = Field(examples=['juancito'], description='')
    password: str = Field(examples=['12345678'], description='')

class ModificarBody(BaseModel):
    nombre: str = Field(default=None, examples=['Juan'], description='')
    apellidos: str = Field(default=None, examples=['Perez'], description='')
    celular: int = Field(default=None, examples=[76543210], description='')
    correo: str = Field(default=None, examples=['juan@perez.com'], description='')
    nacimiento: str = Field(default=None, examples=['01/01/2026'], description='')
    usuario: str = Field(default=None, examples=['juancito'], description='')
    password: str = Field(default=None, examples=['12345678'], description='')

request_elimnar_docente = RequestBody(
    description='',
    content={'application/custom+json': {'schema': get_model_schema(EliminarBody)}}
)

request_registrar_docente = RequestBody(
    description='',
    content={'application/custom+json': {'schema': get_model_schema(RegistrarBody)}}
)

request_modificar_docente = RequestBody(
    description='',
    content={'application/custom+json': {'schema': get_model_schema(ModificarBody)}}
)

class EliminarResponse(Response):
    message: str = Field('El docente fue eliminado correctamente.')
    data: None = Field(None)

class RegistrarResponse(Response):
    code: int = Field(201)
    data: RegistrarBody