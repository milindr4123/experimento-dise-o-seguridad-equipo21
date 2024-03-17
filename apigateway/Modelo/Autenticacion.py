from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import hashlib

from Modelo.Auth import Auth


class Autenticacion(Resource):
    def get(self):      

        data = request.get_json()
        usuario = data.get('usuario')
        contraseña = data.get('contraseña')

        hash_sha256 = hashlib.sha256(contraseña.encode()).hexdigest()

        if usuario != "admin" or hash_sha256 != hash_sha256:
            return jsonify({"msg": "Nombre de usuario o contraseña incorrectos"}), 401
        
        auth_resource = Auth()
        access_token = auth_resource.post()

        return access_token
