from pydantic import BaseModel
from typing import Optional

class TipoDeActividadResponse(BaseModel):
    idTipo: int
    nombre: str
    url: Optional[str]

    class Config:
        from_attributes = True
