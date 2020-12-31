from flask_restful import Resource
from flask import session
from models.avance import AvanceModel


class Avance(Resource):
    def get(self):
        avance = AvanceModel.find_avance_numepoli(session["numepoli"])
        if avance:
            return avance.json(), 200
        return {"message": "Not Avance found"}, 400
