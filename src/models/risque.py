from db import db
from models.assure import AssureModel


class RisqueModel(db.Model):
    __tablename__ = "RISQUE"
    numepoli = db.Column(db.Integer, primary_key=True)
    liberisq = db.Column(db.String(80))
    codeassu = db.Column(db.Integer, db.ForeignKey("RISQUE.codeassu"))
    dateentr = db.Column(db.Date)
    teleassu = db.Column(db.Integer)
    codeinte = db.Column(db.Integer)
    caterisq = db.Column(db.Integer)
    avance = db.relationship("AvanceModel")

    def __init__(
        self, liberisq, codeinte, caterisq, codeassu, dateentr, teleassu, numepoli
    ):
        self.numepoli = numepoli
        self.codeinte = codeinte
        self.caterisq = caterisq
        self.liberisq = liberisq
        self.codeassu = codeassu
        self.dateentr = dateentr
        self.teleassu = teleassu

    @classmethod
    def find_by_numepoli(cls, numepoli):
        return (
            cls.query.filter(
                RisqueModel.numepoli > 0,
                RisqueModel.codeassu > 0,
                RisqueModel.caterisq < 250,
                RisqueModel.caterisq > 239,
                RisqueModel.codeinte != 9999,
            )
            .filter_by(numepoli=numepoli)
            .first()
        )

    def json(self):
        return {
            "numepoli": self.numepoli,
            "codeinte": self.codeinte,
            "caterisq": self.caterisq,
            "liberisq": self.liberisq,
            "codeassu": self.codeassu,
            "dateentr": self.dateentr.strftime("%d/%m/%Y"),
            "teleassu": self.teleassu,
        }
