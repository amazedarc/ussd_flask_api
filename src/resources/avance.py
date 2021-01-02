from flask_restful import Resource
from flask import session
from models.avance import AvanceModel


class Avance(Resource):
    def get(self):
        avances = AvanceModel.find_avance_numepoli(session["numepoli"])
        if avances:
            return [avance.json() for avance in avances], 200
        return {"message": "Not Avance found"}, 400
