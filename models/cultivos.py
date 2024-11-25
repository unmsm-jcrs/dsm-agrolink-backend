from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cultivo(Base):
    __tablename__ = "cultivos"

    idCultivo = Column(Integer, primary_key=True, index=True)
    idUsuario = Column(Integer, nullable=False)
    tipoCultivo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    fechaSiembra = Column(String, nullable=False)
    visibilidad = Column(Integer, nullable=False, default=1)  
    estado = Column(Integer, nullable=False, default=1) 
    fechaCosechado = Column(String, nullable=True)  
