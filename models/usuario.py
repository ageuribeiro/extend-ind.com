# Criando a classe Usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
