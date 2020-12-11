from ..extensions import db

class Status(db.Model):
    __tablename__ = 'Status'

    id_status = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'))
    midia = db.Column(db.String(100), nullable=False)

    def json(self):
        return {
            "id": self.id_status,
            "id_usuario": self.id_usuario,
            "midia": self.midia
        }
