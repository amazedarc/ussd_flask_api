from flask_restful import Resource, reqparse
from flask import session
from models.avance import AvanceModel
from flask_jwt import jwt_required


class Avance(Resource):
    parser = reqparse.RequestParser()

    @jwt_required()
    def post(self):
        pass

    @jwt_required()
    def get(self):
        avances = AvanceModel.find_avance_numepoli(session["numepoli"])
        if avances:
            return [avance.json() for avance in avances], 200
        return {"message": "Not Avance found"}, 400
