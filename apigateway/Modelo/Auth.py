from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

class Auth(Resource):
    def post(self):
        if request.headers.get('X-From-Gateway') == 'true':
            username = request.json.get("username", None)      

            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            return 'Acceso directo no permitido.', 403
        
