from pydantic import BaseModel, Field
from flask_openapi.utils import get_model_schema
from flask_openapi.models.request_body import RequestBody
from features.controllers.validations.ResponseMain import Response

class RegistrarBody(BaseModel):
    nombre_materia: str = Field(examples=['materia1'])
    nivel_estudio: str = Field(examples=['Medio'])
    id_docente: int = Field(examples=[1])
    
request_registrar_mateira = RequestBody(
    description='',
        content={'application/custom+json': {'schema': get_model_schema(RegistrarBody)}}
)

class ModificarBody(BaseModel):
    nombre_materia: str = Field(default=None, examples=['materia1'])
    nivel_estudio: str = Field(default=None, examples=['Medio'])
    id_docente: int = Field(default=None, examples=[1])
    
request_modificar_mateira = RequestBody(
    description='',
        content={'application/custom+json': {'schema': get_model_schema(ModificarBody)}}
)

class EliminarResponse(Response):
    code: int = Field(200)
    message: str = Field('Se elimino la materia correctamente.')

class RegistrarResponse(Response):
    code: int = Field(201)
    data: RegistrarBody
    message: str = Field('Registro de materia con exito..')