from flask_restx import Namespace

api = Namespace('genres')

from . import views
