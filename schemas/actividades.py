from pydantic import BaseModel
from datetime import date

class ActividadBase(BaseModel):
    idCultivo: int
    tipoActividad: int
    fecha: date
    nota: str

class ActividadCreate(ActividadBase):
    pass

class ActividadResponse(ActividadBase):
    idActividad: int

    class Config:
        from_attributes = True
