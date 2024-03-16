from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import requests

url = "http://localhost:5000/entrenamiento"  # Modifica la URL según la configuración de tu servidor Flask


class Entrenamientos(Resource):
    @jwt_required()
    def post(self):
        response = requests.get(url)
    # Verifica si la solicitud fue exitosa (código de estado HTTP 200)
        if response.status_code == 200:
            data = response.json()  # Obtiene los datos de la respuesta en formato JSON
            print(data)
        else:
            print("Error:", response.status_code)
                
