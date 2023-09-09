# models.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, BLOB, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
import db # Certifique-se de importar o objeto db do seu aplicativo Flask

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)



class RatingComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    product = db.relationship('Produto', backref=db.backref('comentarios'), lazy=True)
    client_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    client = db.relationship('Cliente', backref=db.backref('comentarios'), lazy=True)
    rating = db.Column(db.String(100), nullable=True)
    comment = db.Column(db.String(100), nullable=True)
    comment_data = db.Column(db.DateTime, default=datetime.utcnow)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    content = db.Column(db.String(10000), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    category = db.relationship('Categoria', backref=db.backref('blogs', lazy=True))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('blogs', lazy=True))
    published_date = db.Column(db.DateTime, default=datetime.utcnow)


class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),  unique=True, nullable=False)
    value = db.Column(db.String(30),  unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    product = db.relationship('Produto', backref=db.backref('caracteristica'), lazy=True)


class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    product = db.relationship('Produto', backref=db.backref('carrinho'), lazy=True)
    client_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    client = db.relationship('Cliente', backref=db.backref('carrinho'), lazy=True)
    quantity = db.Column(db.Integer,nullable=False)
    value = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(10), unique=True, nullable=False)


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    lastname = db.Column(db.String(100), unique=True, nullable=False)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    cpf =db.Column(db.String(15), unique=True, nullable=False)


class Combo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    imagem = db.Column(db.BLOB, nullable=False)

class Conversa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    client = db.relationship('Cliente', backref=db.backref('conversa'), lazy=True)
    channel = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    last_interaction = db.Column(db.DateTime, nullable=False)


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    hexa = db.Column(db.String(7), unique=True, nullable=False)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    client = db.relationship('Cliente', backref=db.backref('email'), lazy=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    mail = db.Column(db.String(80), unique=True, nullable=False)


class Envio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    order = db.relationship('Pedido', backref=db.backref('envio'), lazy=True)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    status = db.Column(db.String(15), unique=True, nullable=False)

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    country = db.Column(db.String(20), unique=True, nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    client = db.relationship('Cliente', backref=db.backref('cliente'), lazy=True)
    conversa_id = db.Column(db.Integer, db.ForeignKey('conversa.id'))
    conversa = db.relationship('Conversa', backref=db.backref('conversa'), lazy=True)
    rating = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.String(200), nullable=True)


class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(150), unique=False, nullable=True)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    contact = db.Column(db.String(20), unique=True, nullable=False)


class ChatbotIntegration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(20), unique=True, nullable=False)
    token_API = db.Column(db.String(150), unique=False, nullable=True)
    settings = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(50), nullable=False)


class ItemCarrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    cart = db.relationship('Carrinho', backref=db.backref('itemcarrinho'), lazy=True)
    product_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    product = db.relationship('Produto', backref=db.backref('itemcarrinho'), lazy=True)
    value = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)


class ItemCombo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    combo_id = db.Column(db.Integer, db.ForeignKey('combo.id'))
    combo = db.relationship('Combo', backref=db.backref('itemcombo'), lazy=True)
    product_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    product = db.relationship('Produto', backref=db.backref('itemcombo'), lazy=True)
    amount = db.Column(db.Float, nullable=False)


class ItemPromocao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    promotion_id = db.Column(db.Integer, db.ForeignKey('promocao.id'))
    promotion = db.relationship('Promocao', backref=db.backref('itempromocao'), lazy=True)
    product_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    product = db.relationship('Produto', backref=db.backref('itempromocao'), lazy=True)
    price = db.Column(db.Float, unique=False, nullable=False)


class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversa_id = db.Column(db.Integer, db.ForeignKey('conversa.id'))
    conversa = db.relationship('Conversa', backref=db.backref('feedback'), lazy=True)
    tipo = db.Column(db.String(15), nullable=False)
    text = db.Column(db.String(1000), nullable=True)
    mensage_data = db.Column(db.DateTime, default=datetime.utcnow)


class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    order = db.relationship('Pedido', backref=db.backref('pedido'), lazy=True)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    status = db.Column(db.String(15), unique=True, nullable=False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    client = db.relationship('Cliente', backref=db.backref('pedido'), lazy=True)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    status = db.Column(db.String(15), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Identificador do produto
    code_GTIN = db.column(db.String(8)) # Codigo GTIN
    name = db.Column(db.String(20), unique=True, nullable=False) # Nome do Produto
    shortdescription = db.Column(db.String(200), nullable=True) # Descrição curta
    longdescription = db.Column(db.String(400), nullable=True) # descrição longa
    costprice = db.Column(db.Float, unique=False, nullable=False) # preço de custo
    saleprice = db.Column(db.Float, unique=False, nullable=False) # preço de venda
    stock = db.Column(db.Integer, nullable=True) # estoque
    warranty = db.Column(db.Integer, nullable=False) # garantia
    imagem = db.Column(db.BLOB, nullable=False) # imagem
    supplier_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id')) # identificador fornecedor
    supplier = db.relationship('Fornecedor', backref=db.backref('produto'), lazy=True) # fornecedor 
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('fabricante.id')) # identificador fabricante
    manufacturer = db.relationship('Fabricante', backref=db.backref('produto'), lazy=True) #  fabricante 
    size_id = db.Column(db.Integer, db.ForeignKey('tamanho.id')) # identificador do tamanho
    size = db.relationship('Tamanho', backref=db.backref('produto'), lazy=True) # tamanho
    category_id = db.Column(db.Integer, db.ForeignKey('categoria.id')) # identificador da categoria
    category = db.relationship('Categoria', backref=db.backref('produto'), lazy=True) # categoria
    date = db.Column(db.DateTime, unique=True, nullable=False) # data de registro do produto
    status = db.Column(db.String(15), unique=True, nullable=False) # status do produto, se tem muito pouco ou esta na media
    amount = db.Column(db.Float, nullable=False) # quantidade de valor total do produto em estoque

class Promocao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(400), nullable=False)
    startdate = db.Column(db.DateTime, nullable=False) # data de inicio da promoção
    finaldate = db.Column(db.DateTime, nullable=False) # data de finalização da promoção

class RespostChatbot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10000),nullable=False)
    keywords = db.Column(db.String(200), nullable=False)
    answers = db.Column(db.String(10000),nullable=False)

class Tamanho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)