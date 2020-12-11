from ..extensions import db

class Comentario(db.Model):
    __tablename__ = 'Comentário'

    id_comentario = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey('Post.id_post'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'))
    texto = db.Column(db.String(200), nullable=False)

    def json(self):
        return {
            "id": self.id_comentario,
            "id_post": self.id_post,
            "id_usuario": self.id_usuario,
            "texto": self.texto
        }
