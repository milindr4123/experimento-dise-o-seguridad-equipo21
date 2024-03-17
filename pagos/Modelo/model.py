
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_partner = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    account_number = db.Column(db.String(20), nullable=True)
    id_partner = db.Column(db.String(20), nullable=True)
    bank_name = db.Column(db.String(120), nullable=True)
