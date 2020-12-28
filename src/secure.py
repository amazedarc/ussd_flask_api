from models.user import UserModel
import hashlib


def authenticate(numepoli, password):
    user = UserModel.find_by_username(numepoli)
    user_pin = hashlib(user.password.decode())
    if user and user_pin == password:
        return user


def identity(payload):
    userid = payload["identity"]
    return UserModel.find_by_id(userid)