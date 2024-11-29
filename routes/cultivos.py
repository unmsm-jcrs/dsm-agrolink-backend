from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.cultivos import CultivoCreate, CultivoResponse, CultivoUpdate
from models.cultivos import Cultivo
from database import get_db

router = APIRouter()

@router.get("/cultivos/{idUsuario}", response_model=list[CultivoResponse])
def get_cultivos(idUsuario: int, db: Session = Depends(get_db)):
    cultivos = db.query(Cultivo).filter(Cultivo.idUsuario == idUsuario).all()
    if not cultivos:
        raise HTTPException(status_code=404, detail="No se encontraron cultivos para este usuario")
    return cultivos

@router.post("/cultivos", response_model=CultivoResponse)
def create_cultivo(cultivo: CultivoCreate, db: Session = Depends(get_db)):
    db_cultivo = Cultivo(**cultivo.dict())
    db.add(db_cultivo)
    db.commit()
    db.refresh(db_cultivo)
    return db_cultivo

@router.delete("/cultivos/{idCultivo}")
def delete_cultivo(idCultivo: int, db: Session = Depends(get_db)):
    cultivo = db.query(Cultivo).filter(Cultivo.idCultivo == idCultivo).first()
    if not cultivo:
        raise HTTPException(status_code=404, detail="Cultivo no encontrado")
    db.delete(cultivo)
    db.commit()
    return {"message": "Cultivo eliminado correctamente"}

@router.patch("/cultivos/{idCultivo}")
def update_cultivo(idCultivo: int, cultivo_update: CultivoUpdate, db: Session = Depends(get_db)):
    cultivo = db.query(Cultivo).filter(Cultivo.idCultivo == idCultivo).first()
    if not cultivo:
        raise HTTPException(status_code=404, detail="Cultivo no encontrado")

    # Solo actualizamos los campos que no sean None en el objeto cultivo_update
    if cultivo_update.estado is not None:
        cultivo.estado = cultivo_update.estado
    if cultivo_update.visibilidad is not None:
        cultivo.visibilidad = cultivo_update.visibilidad
    if cultivo_update.fechaCosechado is not None:
        cultivo.fechaCosechado = cultivo_update.fechaCosechado
    
    # Guardar los cambios en la base de datos
    db.commit()
    return {"message": "Cultivo actualizado correctamente"}