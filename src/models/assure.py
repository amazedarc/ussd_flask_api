from db import db


class AssureModel(db.Model):
    __tablename__ = "ASSURE"
    codeassu = db.Column(db.Integer, primary_key=True)
    raissoci = db.Column(db.String(80))
    teleassu = db.Column(db.String(80))
    telporas = db.Column(db.String(80))
    codeinte = db.Column(db.Integer)
    prenassu = db.Column(db.String(80))
    numpieid = db.Column(db.String(80))

    def __init__(self, codeassu, raissoci, teleassu, telporas, codeinte):

        self.codeassu = codeassu
        self.raissoci = raissoci
        self.prenassu = prenassu
        self.teleassu = teleassu
        self.telporas = telporas
        self.numpieid = numpieid

    @classmethod
    def find_by_codeassu(cls, codeassu):
        return cls.query.filter(codeassu > 0).filter_by(codeassu=codeassu).first()

    def json(self):
        return {
            "codeinte": self.codeinte,
            "codeassu": self.codeassu,
            "raissoci": self.raissoci,
            "prenassu": self.prenassu,
            "numpieid": self.numpieid,
            "teleassu": self.teleassu,
            "telporas": self.telporas,
        }
