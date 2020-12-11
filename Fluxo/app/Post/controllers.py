from ..extensions import Blueprint, request, jsonify
from .model import Post
from ..extensions import db

post_api = Blueprint('post_api', __name__)

@post_api.route('/posts', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return jsonify([post.json() for post in posts])

    if request.method == 'POST':
        data = request.json

        id_usuario = data.get('id_usuario', None)
        texto = data.get('texto', None)
        midia = data.get('midia', None)

        requirements = [id_usuario, texto, midia]

        if not all(requirement is not None for requirement in requirements):
            return {"erro": "Campos inválidos ou ausentes"},400


        post = Post(
            id_usuario=id_usuario,
            texto=texto,
            midia=midia,
        )
        db.session.add(post)
        db.session.commit()

        return post.json(), 200

@post_api.route('/posts/<int:id>', methods=['GET', 'PATCH'])
def pagina_post(id):
    post = Post.query.get_or_404(id)

    if request.method == 'GET':
        return post.json(),200

    if request.method == 'PATCH':
        data = request.json()

        id_usuario = data.get('id_usuario', post.id_usuario)
        texto = data.get('texto', post.texto)
        midia = data.get('midia', post.midia)

        if id_usuario == '' or texto == '':
            return{"erro": "Campos inválidos ou vazios"}, 400

        post.id_usuario = id_usuario
        post.texto = texto
        post.midia = midia

        db.session.commit()

        return post.json(), 200
