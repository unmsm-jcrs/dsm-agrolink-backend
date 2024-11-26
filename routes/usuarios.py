from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.usuarios import Usuario
from schemas.usuarios import UsuarioCreate, UsuarioLogin
from database import get_db
from hashlib import sha256

router = APIRouter()

def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

@router.post("/usuarios", response_model=UsuarioLogin)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(usuario.contrasenia)
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        contrasenia=hashed_password,
        fechaRegistro=usuario.fechaRegistro,
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Nueva ruta para la autenticación de usuario
@router.post("/login", response_model=UsuarioLogin)
def login_usuario(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    # Buscar el usuario por correo
    db_usuario = db.query(Usuario).filter(Usuario.correo == usuario.correo).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Verificar la contraseña hasheada
    if hash_password(usuario.contrasenia) != db_usuario.contrasenia:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    
    return db_usuario  # Puedes personalizar la respuesta si no quieres devolver toda la información