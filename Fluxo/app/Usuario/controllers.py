from ..extensions import Blueprint, request, jsonify
from .model import Usuario
from ..extensions import db

usuario_api = Blueprint('usuario_api', __name__)

@usuario_api.route('/usuarios', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        usuarios = Usuario.query.all()
        return jsonify([usuario.json() for usuario in usuarios])

    if request.method == 'POST':
        data = request.json

        username = data.get('username', None)
        nickname = data.get('nickname', None)
        userPhoto = data.get('userPhoto', None)
        photoMessage = data.get('photoMessage', None)

        requirements = [username, nickname, userPhoto, photoMessage]

        if not all(requirement is not None for requirement in requirements):
            return {"erro": "Campos inválidos ou ausentes"},400


        usuario = Usuario(
            username=username,
            nickname=nickname,
            userPhoto=userPhoto,
            photoMessage=photoMessage
        )
        db.session.add(usuario)
        db.session.commit()

        return usuario.json(), 200


@usuario_api.route('/usuarios/<int:id>', methods=['GET', 'PATCH'])
def perfil_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'GET':
        return usuario.json(),200

    if request.method == 'PATCH':
        data = request.json()

        username = data.get('username', usuario.username)
        nickname = data.get('nickname', usuario.nickname)
        userPhoto = data.get('userPhoto', usuario.userPhoto)
        photoMessage = data.get('photoMessage', usuario.photoMessage)

        if username == '' or nickname == '':
            return{"erro": "Campos inválidos ou vazios"}, 400

        usuario.username = username
        usuario.nickname = nickname
        usuario.userPhoto = userPhoto
        usuario.photoMessage = photoMessage

        db.session.commit()

        return usuario.json(), 200
