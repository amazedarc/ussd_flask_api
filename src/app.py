from flask import Flask, session
from flask_restful import Api
from flask_jwt import JWT
from resources.item import Item
from resources.user import UserRegister, User, UserList
from resources.assure import Assure, AssureList
from resources.risque import Risque, RisqueList
from resources.avance import Avance
from secure import authenticate, identity

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "oracle://ORASSADM:ora$0car2020@127.0.0.1:1521/SOCARVIE"
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "mazina"

api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:numepoli>")
api.add_resource(UserList, "/users")
api.add_resource(AssureList, "/assures")
api.add_resource(Assure, "/assure/<int:codeassu>")
api.add_resource(Avance, "/avance")
api.add_resource(RisqueList, "/risques")
api.add_resource(Risque, "/risque")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=4800, debug=True)
