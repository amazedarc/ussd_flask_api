from db import db
from uuid import uuid4
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import hashlib
import pytz
from werkzeug.security import generate_password_hash


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(80), nullable=False)
    numepoli = db.Column(db.Integer, nullable=False, unique=True)
    cin = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    telephone = db.Column(db.Integer, nullable=False, unique=True)
    date_naissance = db.Column(
        db.String(15),
        nullable=False,
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow()
        .replace(tzinfo=pytz.utc)
        .astimezone(pytz.timezone("AFRICA/BUJUMBURA")),
        nullable=False,
    )

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
