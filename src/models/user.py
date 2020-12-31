from db import db
from uuid import uuid4
from datetime import datetime
import hashlib
import pytz
from werkzeug.security import generate_password_hash


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80))
    numepoli = db.Column(db.Integer)
    cin = db.Column(db.String(80))
    password = db.Column(db.String(80))
    telephone = db.Column(db.Integer)
    date_naissance = db.Column(db.Date)
    created_at = db.Column(db.Date)
    date_naissance = db.Column(db.Date)

    def __init__(
        self,
        name,
        numepoli,
        cin,
        password,
        telephone,
        date_naissance,
        created_at=None,
    ):
        self.id = uuid4().hex
        self.name = name
        self.numepoli = numepoli
        self.cin = cin
        self.password = hashlib.md5("{}".format(password).encode()).hexdigest()
        self.created_at = (
            datetime.utcnow()
            .replace(tzinfo=pytz.utc)
            .astimezone(pytz.timezone("AFRICA/BUJUMBURA"))
        )
        self.telephone = telephone
        self.date_naissance = datetime.strptime(date_naissance, "%d/%m/%Y")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_numepoli(cls, numepoli):
        return cls.query.filter_by(numepoli=numepoli).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "numepoli": self.numepoli,
            "cin": self.cin,
            "password": self.password,
            "created_at": self.created_at.strftime("%d/%m/%Y"),
            "telephone": self.telephone,
            "date_naissance": self.date_naissance.strftime("%d/%m/%Y"),
        }
