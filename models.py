from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    profile = db.Column(db.Text, nullable=False)
    ativo = db.Column(db.Boolean, default=True)

