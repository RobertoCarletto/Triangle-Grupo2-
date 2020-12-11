from ..extensions import db

class Curtida(db.Model):
    __tablename__ = 'Curtida'

    id_curtida = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey('Post.id_post'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'))

    def json(self):
        return {
            "id": self.id_curtida,
            "id_post": self.id_post,
            "id_usuario": self.id_usuario
        }
