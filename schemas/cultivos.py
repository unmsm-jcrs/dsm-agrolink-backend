from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CultivoBase(BaseModel):
    idUsuario: int
    tipoCultivo: str
    cantidad: float
    fechaSiembra: datetime
    visibilidad: int
    estado: int
    fechaCosechado: Optional[datetime] = None

class CultivoCreate(CultivoBase):
    pass

class CultivoUpdate(BaseModel):
    estado: Optional[int] = None
    visibilidad: Optional[int] = None
    fechaCosechado: Optional[datetime] = None

class CultivoResponse(CultivoBase):
    idCultivo: int

    class Config:
        from_attributes  = True
