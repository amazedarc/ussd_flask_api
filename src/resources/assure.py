from models.assure import AssureModel
from flask_restful import Resource
from flask_jwt import jwt_required
from flask import session
from models.risque import RisqueModel


class Assure(Resource):
    @jwt_required()
    def get(self):
        risque = RisqueModel.find_by_numepoli(session["numepoli"])
        assure = AssureModel.find_by_codeassu(risque.codeassu)
        if assure:
            return assure.json(), 200
        return {"message": "assure not found"}, 400


class AssureList(Resource):
    @jwt_required()
    def get(self):
        # return {'items': list(map(lambda item: item.json(), ItemModel.query.all()))}
        return {"Assures": [assure.json() for assure in AssureModel.query.all()]}
