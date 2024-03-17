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
    
    @jwt_required()
    def put(self):
        payment_request = request.json
        payment = Pago.query.get_or_404(payment_request["id_pago"])
        payment.name_partner = payment_request["nombre"]
        payment.account_number = payment_request["numero_cuenta"]
        payment.email = payment_request["correo"]
        payment.id_partner = payment_request["cedula"]
        payment.bank_name = payment_request["banco"]        
        db.session.commit()

        msg = Message('Actualización de información bancaria',
                      sender='your_email@example.com',
                      recipients=[payment.email])
        msg.body = f'Hola {payment.name_partner}, tu información de pagos se ha actualizado correctamente.'
        mail.send(msg)

        flash('¡Información bancaria actualizada!')
