from flask import Flask
from .config import  Config
from .extensions import db,migrate
from .Usuario.controllers import usuario_api
from .Post.controllers import post_api
from .Status.controllers import status_api
from .Comentario.controllers import comentario_api
from .Curtida.controllers import curtida_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(usuario_api)
    app.register_blueprint(post_api)
    app.register_blueprint(status_api)
    app.register_blueprint(comentario_api)
    app.register_blueprint(curtida_api)

    return app
