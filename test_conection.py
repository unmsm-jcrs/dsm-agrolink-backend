from sqlalchemy import text
from database import engine

def test_connection():
    try:
        # Establecer conexión
        with engine.connect() as connection:
            # Ejecutar una consulta válida (usando text())
            result = connection.execute(text("SELECT 1")).fetchone()
            print("Conexión exitosa:", result)
    except Exception as e:
        print("Error al conectar:", str(e))

if __name__ == "__main__":
    test_connection()