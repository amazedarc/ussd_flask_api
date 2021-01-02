from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel
import hashlib
from models.risque import RisqueModel
from models.assure import AssureModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "name", type=str, required=True, help="The user name filed can not be empty"
    )
    parser.add_argument(
        "numepoli",
        type=int,
        required=True,
        help="The user numepoli filed can not be empty",
    )
    parser.add_argument(
        "telephone",
        type=str,
        required=True,
        help="The user telephone filed can not be empty",
    )
    parser.add_argument(
        "cin", type=str, required=True, help="The user CIN filed can not be empty"
    )
    parser.add_argument(
        "password",
        type=int,
        required=True,
        help="The user password filed can not be empty",
    )
    parser.add_argument(
        "date_naissance",
        type=str,
        required=True,
        help="The user birthday date filed can not be empty",
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_numepoli(data.numepoli)

        if user is None:
            risque = RisqueModel.find_by_numepoli(data.numepoli)
            if risque is not None and risque.numepoli == data.numepoli:
                assure = AssureModel.find_by_codeassu(risque.codeassu)
                if assure.teleassu != data.telephone:
                    return {"message": "Your number doesn't match the existing one"}
                user = UserModel(**data)
            user.save_to_db()
        else:
            return {"message": "user with numepoli {} exist".format(data.numepoli)}, 400

        return {"message": "User has been created"}


class User(Resource):
    @jwt_required()
    def get(self, numepoli):
        risque_data = RisqueModel.find_by_numepoli(numepoli)
        user = UserModel.find_by_numepoli(numepoli)
        if risque_data:
            return risque_data.json(), 200
        return {"message": "user not found {}".format(risque_data)}, 400


class UserList(Resource):
    @jwt_required()
    def get(self):
        return {"users": [user.json() for user in UserModel.query.all()]}
