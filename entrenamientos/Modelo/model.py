
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Entrenamiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    account_number = db.Column(db.String(20), nullable=True)
    cedula = db.Column(db.String(20), nullable=True)
    bank_name = db.Column(db.String(120), nullable=True)
