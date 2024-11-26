from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TipoDeActividad(Base):
    __tablename__ = 'tipo_actividad'
    
    idTipo = Column(Integer, primary_key=True)
    url = Column(String, nullable=True)
    nombre = Column(String, nullable=True)
