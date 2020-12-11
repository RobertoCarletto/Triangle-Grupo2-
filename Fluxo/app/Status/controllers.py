from ..extensions import Blueprint, request, jsonify
from .model import Status
from ..extensions import db

status_api = Blueprint('status_api', __name__)

@status_api.route('/status', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        statuses = Status.query.all()
        return jsonify([status.json() for status in statuses])

    if request.method == 'POST':
        data = request.json

        id_usuario = data.get('id_usuario', None)
        midia = data.get('midia', None)

        requirements = [id_usuario, midia]

        if not all(requirement is not None for requirement in requirements):
            return {"erro": "Campos inválidos ou ausentes"},400


        status = Status(
            id_usuario=id_usuario,
            midia=midia,
        )

        db.session.add(status)
        db.session.commit()

        return status.json(), 200

@status_api.route('/status/<int:id>', methods=['GET', 'PATCH'])
def pagina_status(id):
    status = Status.query.get_or_404(id)

    if request.method == 'GET':
        return status.json(),200

    if request.method == 'PATCH':
        data = request.json()

        id_usuario = data.get('id_usuario', status.id_usuario)
        midia = data.get('midia', status.midia)

        if id_usuario == '' or midia == '':
            return{"erro": "Campos inválidos ou vazios"}, 400

        status.id_usuario = id_usuario
        status.midia = midia

        db.session.commit()

        return status.json(), 200
