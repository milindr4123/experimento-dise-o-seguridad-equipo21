#from base import Entrenamiento
from flask import jsonify, flash, request
from flask_mail import Mail, Message
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from Modelo.model import db, Pago
mail = Mail()

class PagosResource(Resource):

    @jwt_required()
    def post(self):
        user = request.json
        new_user = Pago(name_partner=user["nombre"], account_number=user["numero_cuenta"], email=user["correo"], id_partner=user["cedula"], bank_name=user["banco"])
        db.session.add(new_user)
        db.session.commit()
        return 'Usuario creado con éxito!'
    
    def put(self, id_pago, nombre, numero_cuenta, correo, cedula, banco):
        user = Pago.query.get_or_404(id_pago)
        user.account_number = numero_cuenta
        user.name_partner = nombre
        user.id_partner = cedula
        user.bank_name = banco
        user.email = correo        

        msg = Message('Actualización de información bancaria',
                      sender='your_email@example.com',
                      recipients=[user.email])
        msg.body = f'Hola {user.username}, tu información bancaria se ha actualizado correctamente.'
        mail.send(msg)

        flash('¡Información bancaria actualizada!')
