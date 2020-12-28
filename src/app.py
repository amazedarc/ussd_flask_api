from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.store import Store
from resources.item import Item
from resourses.user import User
from secure import authenticate, identity

app = Flask(__name__)
api = Api(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "oracle://ORASSADM:ora$0car2020@127.0.0.1:1521/SOCARVIE"
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

jwt = JWT(app, authenticate, identity)
if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=4200, debug=True)

api.add_resource(User, "/user/<string:numepoli>")
# api.add_resource(Item, "/item/<string:name>")
