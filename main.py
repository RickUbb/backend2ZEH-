"""
main.py

Este módulo inicializa y ejecuta la aplicación Flask.
"""

from src import init_app
import sys


def initialize_app():
    """
    Inicializa la aplicación Flask.
    """
    try:
        return init_app()
    except Exception as e:
        raise RuntimeError(f"Error al inicializar la aplicación: {e}")


if __name__ == '__main__':
    """
    Este bloque se ejecuta solo si el archivo es ejecutado directamente.
    """
    try:
        app = initialize_app()
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"Error al iniciar el servidor Flask: {e}", file=sys.stderr)
