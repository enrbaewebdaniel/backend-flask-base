from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

def init_db(app):
    """Inicializa la base de datos, creando las tablas."""
    with app.app_context():
        database.create_all()
