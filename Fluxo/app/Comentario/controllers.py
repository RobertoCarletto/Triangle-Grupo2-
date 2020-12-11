from ..extensions import Blueprint, request, jsonify
from .model import Comentario
from ..extensions import db

comentario_api = Blueprint('comentario_api', __name__)

@comentario_api.route('/comentarios', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        comentarios = Comentario.query.all()
        return jsonify([comentario.json() for comentario in comentarios])

    if request.method == 'POST':
        data = request.json

        id_post = data.get('id_post', None)
        id_usuario = data.get('id_usuario', None)
        texto = data.get('texto', None)

        requirements = [id_post, id_usuario, texto]

        if not all(requirement is not None for requirement in requirements):
            return {"erro": "Campos inválidos ou ausentes"},400


        comentario = Comentario(
            id_post=id_post,
            id_usuario=id_usuario,
            texto=texto,
        )
        db.session.add(comentario)
        db.session.commit()

        return comentario.json(), 200


@comentario_api.route('/comentarios/<int:id>', methods=['GET', 'PATCH'])
def perfil_comentario(id):
    comentario = Comentario.query.get_or_404(id)

    if request.method == 'GET':
        return comentario.json(),200

    if request.method == 'PATCH':
        data = request.json()

        id_post = data.get('id_post', comentario.id_post)
        id_usuario = data.get('id_usuario', comentario.id_usuario)
        texto = data.get('texto', comentario.texto)

        if id_post == '' or id_usuario == '':
            return{"erro": "Campos inválidos ou vazios"}, 400

        comentario.id_post = id_post
        comentario.id_usuario = id_usuario
        comentario.texto = texto

        db.session.commit()

        return comentario.json(), 200

