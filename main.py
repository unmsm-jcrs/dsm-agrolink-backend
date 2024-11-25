from fastapi import FastAPI
from routes import cultivos
from database import Base, engine

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar rutas
app.include_router(cultivos.router, prefix="/api", tags=["Cultivos"])

@app.get("/")
def root():
    return {"message": "API de Cultivos lista"}
