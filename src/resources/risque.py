from models.risque import RisqueModel
from flask_restful import Resource
from flask_jwt import jwt_required
from flask import session


class Risque(Resource):
    @jwt_required()
    def get(self):
        risque = RisqueModel.find_by_numepoli(session["numepoli"])
        if risque:
            return risque.json(), 200
        return {"message": "assure not found"}, 400


class RisqueList(Resource):
    @jwt_required()
    def get(self):
        # return {'items': list(map(lambda item: item.json(), ItemModel.query.all()))}
        return {"Risques": [risque.json() for risque in RisqueModel.query.all()]}
