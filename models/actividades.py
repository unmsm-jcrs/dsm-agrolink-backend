from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Actividad(Base):
    __tablename__ = "actividades_agricolas"

    idActividad = Column(Integer, primary_key=True, index=True)
    idCultivo = Column(Integer, nullable=True)
    tipoActividad = Column(Integer, nullable=True)
    fecha = Column(Date, nullable=True)
    nota = Column(Text, nullable=True)
