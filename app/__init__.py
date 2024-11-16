from flask import Flask
from app.extensions import database, init_db
from app.routes import register_routes
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    database.init_app(app)
    init_db(app)

    # Registrar rutas
    register_routes(app)

    return app
