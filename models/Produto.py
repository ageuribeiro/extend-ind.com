# Criando a classe Produto
class Produto(db.Model):
    __tablename__='produtos'
    id = db.Column(db.Integer, primary_key=True)
    cod = db.Column(db.String(50),nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Product {self.id}>'
