from pydantic import BaseModel
from typing import Optional

class CultivoBase(BaseModel):
    idUsuario: int
    tipoCultivo: str
    cantidad: float
    fechaSiembra: str
    visibilidad: int
    estado: int
    fechaCosechado: Optional[str] = None

class CultivoCreate(CultivoBase):
    pass

class CultivoResponse(CultivoBase):
    idCultivo: int

    class Config:
        orm_mode = True
