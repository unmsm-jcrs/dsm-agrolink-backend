from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    idUsuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(50), nullable=False, unique=True)
    contrasenia = Column(Text, nullable=False)
    fechaRegistro = Column(DateTime, nullable=False)