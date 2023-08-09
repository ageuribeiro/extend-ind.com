from database import db

# Criando a classe Usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email, senha, cpf, username, senha):
        self.nome = nome
        self.email =  email
        self.senha = senha
        self.cpf = cpf
        self.username = username
        self.senha = senha

    def __repr__(self):
        return 'Usuario: {}'.format(self.username)


# Criando a classe Produto
class Produto(db.Model):
    __tablename__='produto'
    id = db.Column(db.Integer, primary_key=True)
    cod = db.Column(db.String(50),nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    def __init__(self, cod, nome, preco, descricao):
        self.cod = cod
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
    def __repr__(self):
        return 'Produto: {}'.format(self.cod)
