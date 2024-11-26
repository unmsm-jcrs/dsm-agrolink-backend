from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.tipoActividades import TipoDeActividadResponse
from models.tipoActividades import TipoDeActividad
from database import get_db

router = APIRouter()

# Obtener tipos de actividad
@router.get("/tipos", response_model=list[TipoDeActividadResponse])
def get_tipos_de_actividad(db: Session = Depends(get_db)):
    tipos_actividad = db.query(TipoDeActividad).all()
    if not tipos_actividad:
        raise HTTPException(status_code=404, detail="No se encontraron tipos de actividad")
    return tipos_actividad
