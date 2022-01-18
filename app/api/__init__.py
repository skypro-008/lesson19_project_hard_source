from flask import Blueprint
from flask_restx import Api

from .directors import api as director_ns
from .genres import api as genre_ns
from .movies import api as movie_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint,
          title='My Title',
          version='1.0',
          description='A description',
          )

api.add_namespace(director_ns)
api.add_namespace(genre_ns)
api.add_namespace(movie_ns)
