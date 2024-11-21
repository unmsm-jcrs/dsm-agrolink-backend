from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import cultivos, usuarios, clima, actividades, sesiones

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
        "http://127.0.0.1:8000"
        ],  # Poner lo de devtunel
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(cultivos.router)
app.include_router(usuarios.router)
app.include_router(clima.router)
app.include_router(actividades.router)
app.include_router(sesiones.router)