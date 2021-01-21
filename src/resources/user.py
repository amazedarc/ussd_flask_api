from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from werkzeug.security import safe_str_cmp
from flask_jwt import jwt_required
from models.user import UserModel
import hashlib
from models.risque import RisqueModel
from models.assure import AssureModel
from schemas.users import Userschema

user_schema = Userschema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        try:
            user_data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_numepoli(user_data["numepoli"]):
            return {
                "message": "user with numepoli {} exist".format(user_data["numepoli"])
            }, 400
        user = UserModel(**user_data)
        user.save_to_db()
        return {"message": "User has been created"}, 201


class User(Resource):
    @jwt_required()
    def get(self, numepoli):
        risque_data = RisqueModel.find_by_numepoli(numepoli)
        user = UserModel.find_by_numepoli(numepoli)
        if not risque_data:
            return {"message": "User {} not found ".format(risque_data.numepoli)}, 400
        return user_schema.dump(user), 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        try:
            user_data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        user = UserModel.find_by_numepoli(user_data.numepoli)

        if user and safe_str_cmp(user.password, user_data["PASSWORD"]):
            pass


class UserList(Resource):
    @jwt_required()
    def get(self):
        return {"users": [user.json() for user in UserModel.query.all()]}
