from flask_restx import Resource
from . import api
from app import db

from .models import GenreSchema
from .dao import GenreDAO
from .services import GenreService

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)


@api.route('/')
class GenresView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@api.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
