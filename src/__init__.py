"""
src.__init__.py

Este módulo inicializa la aplicación Flask y configura sus componentes principales,
incluyendo el registro de blueprints y la configuración de CORS.
"""

from flask import Flask
from flask_cors import CORS
from src.routes.SolarPanelRoutes import solar

app = Flask(__name__)
CORS(app)


def init_app():
    """
    Inicializa la aplicación Flask y registra los blueprints requeridos.

    Returns:
        Flask: Instancia configurada de la aplicación Flask.
    """
    try:
        app.register_blueprint(solar, url_prefix='/api/v1/solar')
        return app
    except Exception as e:
        raise RuntimeError(f"Error al registrar las rutas: {e}")
