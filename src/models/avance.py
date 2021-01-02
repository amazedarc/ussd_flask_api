from db import db


class AvanceModel(db.Model):
    __tablename__ = "AVANCE"
    numepoli = db.Column(db.Integer, primary_key=True)
    codeinte = db.Column(db.Integer)
    codeassu = db.Column(db.Integer)
    numeavan = db.Column(db.Integer)
    dateavan = db.Column(db.Date)
    montavan = db.Column(db.Integer)
    dureremb = db.Column(db.Integer)
    montremb = db.Column(db.Integer)
    reliremb = db.Column(db.Integer)

    def __init__(
        self,
        codeinte,
        numepoli,
        codeassu,
        numeavan,
        dateavan,
        montavan,
        dureremb,
        montremb,
        reliremb,
    ):
        self.codeinte = codeinte
        self.numepoli = numepoli
        self.codeassu = codeassu
        self.numeavan = numeavan
        self.dateavan = dateavan
        self.montavan = montavan
        self.dureremb = dureremb
        self.montremb = montremb
        self.reliremb = reliremb

    @classmethod
    def find_avance_numepoli(cls, numepoli):
        return cls.query.filter_by(numepoli=numepoli).all()

    def json(self):
        return {
            "codeinte": self.codeinte,
            "numepoli": self.numepoli,
            "codeassu": self.codeassu,
            "numeavan": self.numeavan,
            "dateavan": self.dateavan.strftime("%d/%m/%Y"),
            "montavan": self.montavan,
            "dureremb": self.dureremb,
            "montremb": self.montremb,
            "reliremb": self.reliremb,
        }
