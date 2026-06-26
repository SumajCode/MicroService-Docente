from pydantic import BaseModel, Field
from typing import Any

class Response(BaseModel):
    code: int = Field(200)
    data: Any | None
    message: str