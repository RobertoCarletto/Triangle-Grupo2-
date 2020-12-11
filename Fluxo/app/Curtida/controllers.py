from ..extensions import Blueprint, request, jsonify
from .model import Curtida
from ..extensions import db

curtida_api = Blueprint('curtida_api', __name__)

@curtida_api.route('/curtida', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        curtidas = Curtida.query.all()
        return jsonify([curtida.json() for curtida in curtidas])

    if request.method == 'POST':
        data = request.json

        id_usuario = data.get('id_usuario', None)
        id_post = data.get('id_post', None)

        requirements = [id_usuario, id_post]

        if not all(requirement is not None for requirement in requirements):
            return {"erro": "Campos inválidos ou ausentes"},400


        curtida = Curtida(
            id_usuario=id_usuario,
            id_post=id_post,
        )

        db.session.add(curtida)
        db.session.commit()

        return curtida.json(), 200

@curtida_api.route('/curtida/<int:id>', methods=['GET', 'PATCH'])
def pagina_curtida(id):
    curtida = Curtida.query.get_or_404(id)

    if request.method == 'GET':
        return curtida.json(),200

    if request.method == 'PATCH':
        data = request.json()

        id_usuario = data.get('id_usuario', curtida.id_usuario)
        id_post = data.get('id_post', curtida.id_post)

        if id_usuario == '' or id_post == '':
            return{"erro": "Campos inválidos ou vazios"}, 400

        curtida.id_usuario = id_usuario
        curtida.id_post = id_post

        db.session.commit()

        return curtida.json(), 200
