from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from Modelo.Auth import Auth
from Modelo.Protected import Protected


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "tu_super_secreto_secreto"  # Cambia esto por una llave secreta real
    jwt = JWTManager(app)

    api.add_resource(Auth, "/auth")
    api.add_resource(Protected, "/protected")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
