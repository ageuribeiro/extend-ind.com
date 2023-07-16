from flask import Flask, render_template, redirect, flash, request, send_file, send_from_directory, session, url_for
from flask_sqlalchemy import SQLAlchemy
from config import *
import secrets
import psycopg2

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# Configuração da primeira conexão ao banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://admin:0FgeMTgVOt74NjHIHPTGVr4xwkQeYPOK@dpg-cipk1td9aq0dcpqkq3hg-a.oregon-postgres.render.com/database_bemchique'

# Configuração da segunda conexão ao banco de dados (URL interna)
app.config['SQLALCHEMY_BINDS'] = {'internal_db': 'postgres://admin:0FgeMTgVOt74NjHIHPTGVr4xwkQeYPOK@dpg-cipk1td9aq0dcpqkq3hg-a/database_bemchique'}

# Define a rota principal para o usuario
@app.route("/")
def home():
    categorias = ['Blusas', 'Camisetas', 'Saias', 'Sapatos', 'Relógios', 'Maquiagem', 'Promoções']
    return render_template(
        "index.html", 
        categorias=categorias,
        title='Showcase',
        endereco_loja=endereco_loja,
        texto_destaque=texto_destaque,
        whatsapp=whatsapp,
        nome_loja=nome_loja,
        whatsapp_link=whatsapp_link,
        email=email,
        telefone=telefone,
        instagram_link=instagram_link)

# Define a rota principal para o Administrador
@app.route("/admin")
def admin():
    return render_template("admin/index.html", title='Home')

# Define a rota principal para o Administrador
@app.route("/admin/login")
def admin_login():
    return render_template("admin/login.html", title='Login')

# Define a rota principal para o Administrador
@app.route("/admin/verify_account")
def admin_verify_account():
    return render_template("admin/verify_account.html", title='Verifying')

# Define a rota para página Produtos
@app.route('/produtos')
def produtos():
    return render_template('produtos/produtos.html')

# Define a rota para a página de Lista de Produtos
@app.route('/lista_produtos')
def lista_produtos():
    return render_template('produtos/lista-produtos.html')

# Define a rota para a página Sistemas
@app.route('/sistemas')
def sistemas():
    return render_template('sistema')

# Define a rota para a página de Categorias
@app.route('/categorias')
def categorias():
    return render_template('estrutura/categorias.html')

# Define a rota para a página de Promoções
@app.route('/promotions')
def promotions():
    return render_template('estrutura/promocoes.html')

# Define a rota para a página Contatos
@app.route('/contatos')
def contatos():
    return render_template('estrutura/contatos.html')

# Define a rota para a página Sobre
@app.route('/sobre')
def sobre():
    return render_template('estrutura/sobre.html')

# Define a rota par a página Carrinhos
@app.route('/carrinho')
def carrinho():
    return render_template('estrutura/carrinho.html')

# Define a rota para a página Blog
@app.route('/blog')
def blog():
    return render_template('estrutura/blog.html')

db = SQLAlchemy(app)
if __name__ == '__main__':
    # Cria as tabelas no banco de dados
    db.create_all()

    # Inicia o servidor flask
    app.run(debug=True, port=9000)