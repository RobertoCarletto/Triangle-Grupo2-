from ..extensions import db


class Post(db.Model):
    __tablename__ = 'Post'

    id_post = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'))
    texto = db.Column(db.String(200), nullable=False)
    midia = db.Column(db.String(100))

    curtidas = db.relationship('Curtida', backref='Post')
    comentarios = db.relationship('Comentario', backref='Post')

    def json(self):
        return {
            "id": self.id_post,
            "id_usuario": self.id_usuario,
            "texto": self.texto,
            "midia": self.midia
        }
