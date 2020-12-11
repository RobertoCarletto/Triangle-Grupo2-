from ..extensions import db



class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    nickname = db.Column(db.String(30), nullable=False)
    userPhoto = db.Column(db.String(100), nullable=False)
    photoMessage = db.Column(db.String(30), nullable=False)


    seguindo = db.relationship('Usuario',
        lambda: seguidores,
        primaryjoin=lambda: Usuario.id_usuario == seguidores.c.id_usuario,
        secondaryjoin=lambda: Usuario.id_usuario == seguidores.c.id_usuario_seguido,
        backref='seguido'
    )


    posts = db.relationship('Post', backref='Usuario')
    status = db.relationship('Status', backref='Usuario')

    def json(self):
        return {
            "id": self.id_usuario,
            "username": self.username,
            "nickname": self.nickname,
            "userPhoto": self.userPhoto,
            "photoMessage": self.photoMessage
        }

seguidores = db.Table('seguidores',
    db.Column('id_usuario', db.Integer, db.ForeignKey('Usuario.id_usuario'), primary_key=True),
    db.Column('id_usuario_seguido', db.Integer, db.ForeignKey('Usuario.id_usuario'), primary_key=True)
)
