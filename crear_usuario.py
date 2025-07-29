from app import create_app, db
from app.models import Usuario  # Ajusta el path según tu estructura

app = create_app()

with app.app_context():
    existe = Usuario.query.filter_by(celular="123456").first()
    if existe:
        print("Ya existe un usuario admin.")
    else:
        nuevo_usuario = Usuario(
            nombre="admin",
            apellido="general",
            celular="123456",
            password="admin123",
            tipo_usuario=1,
            usuario_verificado=True
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        print("Usuario admin creado con éxito")