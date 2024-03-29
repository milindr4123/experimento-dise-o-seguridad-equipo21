from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from Modelo.Autenticacion import Autenticacion
from Modelo.Entrenamientos import Entrenamientos
from Modelo.Pagos import Pago
import requests

GATEWAY_HEADER = 'X-From-Gateway'

def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "tu_super_secreto_secreto"  # Cambia esto por una llave secreta real
    jwt = JWTManager(app)

    api.add_resource(Autenticacion, "/autenticacion")
    api.add_resource(Entrenamientos, "/entrenamientos")
    api.add_resource(Pago, "/pago")
    
    @app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT'])
    def proxy(path):
        SERVICES = {
            'autenticacion',
            'entrenamientos',
            'pago',
        }


        if path in SERVICES:
            
            request.environ.setdefault('HTTP_X_FROM_GATEWAY', 'true')

            print(request.headers)

            response = requests.request(
                method=request.method,
                url=f"http://localhost:5000/{path}",
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
