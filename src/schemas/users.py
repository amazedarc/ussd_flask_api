from models.user import UserModel
from ma import ma


class Userschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
