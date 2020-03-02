"""
Sample demo routes
"""

from flask import Blueprint

MAIN_VIEWS = Blueprint('main_views', __name__)


@MAIN_VIEWS.route('/')
def hello_world():
    return 'Flask Dockerized'
