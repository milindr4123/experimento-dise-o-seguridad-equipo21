from base import app, api, Entrenamiento, Resource
from flask import jsonify

class EntrenamientoResource(Resource):
    def post(self, nombre, numero_cuenta):
        new_user = Entrenamiento(nombre,
            numero_cuenta)
        

        return jsonify(user=new_user)



api.add_resource(EntrenamientoResource, '/entrenamiento')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
