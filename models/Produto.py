class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod = db.Column(db.String(50),nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return f"Produto(id={self.id},código={self.cod},nome={self.nome},preco={self.preco}, descrição={self.descricao})"