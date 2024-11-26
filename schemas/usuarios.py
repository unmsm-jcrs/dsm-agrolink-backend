from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    fechaRegistro: datetime

class UsuarioCreate(UsuarioBase):
    contrasenia: str

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasenia: str

    class Config:
        from_attributes  = True
