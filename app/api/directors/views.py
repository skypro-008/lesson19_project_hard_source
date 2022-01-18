from flask_restx import Resource
from . import api
from app import db
from .models import DirectorSchema
from .dao import DirectorDAO
from .services import DirectorService

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(dao=director_dao)


@api.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@api.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
