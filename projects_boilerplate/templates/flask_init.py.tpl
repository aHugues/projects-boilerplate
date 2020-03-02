"""
Main package for the application
"""

from flask import Flask

from .views import MAIN_VIEWS


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(MAIN_VIEWS)
    return app
