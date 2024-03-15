from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

class Auth(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        if username != "admin" or password != "secret":
            return jsonify({"msg": "Nombre de usuario o contraseña incorrectos"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
