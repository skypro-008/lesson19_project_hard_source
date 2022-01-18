from flask_restx import Namespace

api = Namespace('movies')

from . import views
