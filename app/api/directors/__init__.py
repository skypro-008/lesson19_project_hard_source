from flask_restx import Namespace

api = Namespace('directors')

from . import views
