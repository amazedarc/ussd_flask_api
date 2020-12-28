from db import db
from uuid import uuid4
from datetime import datetime
import hashlib


class UserModel:
    __tablename__: "risque_user"
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80))
    numepoli = db.Column(db.Integer)
    cin = db.Column(db.String(80))
    password = db.Column(db.String(80))
    telephone = db.Column(db.Integer)
    date_naissance = db.Column(db.Date)
    created_at = db.Column(db.Date)
    self.telephone = db.Column(db.Integer)
    self.date_naissance = datetime.datetime.strptime(date_naissance, "%d/%m/%Y")

    def __init__(
        self,
        _id,
        name,
        numepoli,
        cin,
        password,
        telephone,
        date_naissance,
        created_at=None,
    ):
        self.id = uuid4().hex if _id is None else _id
        self.name = name
        self.numepoli = numepoli
        self.cin = cin
        self.password = hashlib.md5(password.encode())
        self.created_at = (
            datetime.datetime.utcnow() if created_at is None else created_at
        )
        self.telephone = telephone
        self.date_naissance = datetime.datetime.strptime(date_naissance, "%d/%m/%Y")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_numepoli(cls, numepoli):
        return cls.query.filter_by(numepoli=numepoli).first()
