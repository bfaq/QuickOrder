import os
from app import create_app, db  # Asegúrate de que "app" sea el nombre de tu paquete
import psycopg2
import time


# Creamos la app usando tu factory
app = create_app()

def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
            host="db",
            database="Proyectocloud",
            user="postgres",
            password="Talon1528"
            )
            conn.close()
            print("✅ PostgreSQL está listo")
            break
        except psycopg2.OperationalError:
            print("⏳ Esperando a PostgreSQL...")
            time.sleep(2)

if __name__ == "__main__":
    # Activa el modo debug y el recargador automático
    wait_for_postgres()
    with app.app_context():
        db.create_all()
    app.run(
        debug=True,
        host="0.0.0.0",  # Para permitir conexiones externas (opcional)
        port=int(os.environ.get("PORT", 5000))  # Usa el puerto 5000 por defecto
    )
