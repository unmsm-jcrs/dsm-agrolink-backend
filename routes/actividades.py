from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.actividades import ActividadCreate, ActividadResponse
from models.actividades import Actividad
from database import get_db

router = APIRouter()

# Obtener actividades por cultivo
@router.get("/actividades/{idCultivo}", response_model=list[ActividadResponse])
def get_actividades(idCultivo: int, db: Session = Depends(get_db)):
    actividades = db.query(Actividad).filter(Actividad.idCultivo == idCultivo).all()
    if not actividades:
        raise HTTPException(status_code=404, detail="No se encontraron actividades para este cultivo")
    return actividades

# Crear una nueva actividad
@router.post("/actividades", response_model=ActividadResponse)
def create_actividad(actividad: ActividadCreate, db: Session = Depends(get_db)):
    db_actividad = Actividad(**actividad.dict())
    db.add(db_actividad)
    db.commit()
    db.refresh(db_actividad)
    return db_actividad

# Eliminar una actividad por ID
@router.delete("/actividades/{idActividad}")
def delete_actividad(idActividad: int, db: Session = Depends(get_db)):
    actividad = db.query(Actividad).filter(Actividad.idActividad == idActividad).first()
    if not actividad:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    db.delete(actividad)
    db.commit()
    return {"message": "Actividad eliminada correctamente"}
