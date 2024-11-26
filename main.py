from fastapi import FastAPI
from routes import cultivos, usuarios, actividades,tipoActividades
from database import Base, engine

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar rutas
app.include_router(cultivos.router, prefix="/api", tags=["Cultivos"])
app.include_router(usuarios.router, prefix="/api", tags=["Usuarios"])
app.include_router(actividades.router, prefix="/api", tags=["Actividades"])
app.include_router(tipoActividades.router, prefix="/api", tags=["Tipos"])

@app.get("/")
def root():
    return {"message": "API de Cultivos lista"}
