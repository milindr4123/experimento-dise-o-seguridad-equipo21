from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from Modelo.model import db
from Modelo.Auth import Auth
from Modelo.Protected import Protected
from api_commands import PagosResource
from flask_mail import Mail

import requests

GATEWAY_HEADER = 'X-From-Gateway'

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pagos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'arquitecturaagil@gmail.com'
    app.config['MAIL_PASSWORD'] = '4rquitecturas@'

    mail = Mail(app)

    app_context = app.app_context()
    app_context.push()

    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "tu_super_secreto_secreto"
    jwt = JWTManager(app)

    api.add_resource(PagosResource, "/pago")

    
    @app.route('/api2/<path:path>', methods=['GET', 'POST', 'PUT'])
    def proxy(path):
        SERVICES = {
            'pago'
        }


        if path in SERVICES:
            
            request.environ.setdefault('HTTP_X_FROM_GATEWAY', 'true')

            print(request.headers)

            response = requests.request(
                method=request.method,
                url=f"http://localhost:5002/{path}",
                headers=request.headers,
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False
            )

            return response.content, response.status_code, response.headers.items()
        else:
            return jsonify({'error': 'Servicio no encontrado'}), 404

    return app

app = create_app()
db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)