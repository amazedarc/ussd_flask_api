from flask import session
from models.user import UserModel
import hashlib


def authenticate(numepoli, password):
    user = UserModel.find_by_numepoli(numepoli)
    password_hash = hashlib.md5("{}".format(password).encode()).hexdigest()
    if user and user.password == password_hash:
        session["numepoli"] = user.numepoli
        return user


def identity(payload):
    userid = payload["identity"]
    return UserModel.find_by_id(userid)
