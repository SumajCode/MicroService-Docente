from pydantic import BaseModel, Field
from flask_openapi.openapi import RequestBody
from flask_openapi.utils import get_model_schema
# * Create two models class of pydantic to aggregate responses and body example
class EliminarBody(BaseModel):
    id: int = Field(examples=[1], description='Id del docente a eliminar')

request_elimnar_docente = RequestBody(
    description='',
    content={'application/custom+json': {'schema': get_model_schema(EliminarBody)}}
)

class EliminarResponse(BaseModel):
    code: int = Field(examples=[200], description='Code')
    