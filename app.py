from flask import Flask, render_template, redirect, flash, request, send_file, send_from_directory, session, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import config
import conexao
import secrets
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bemchique_db.db'
db = SQLAlchemy(app)
app.secret_key = secrets.token_hex(16)

# Criando as classes
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_cpf = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod = db.Column(db.String(50),nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=False)

# Verificar Credenciais
def verificar_credenciais(email_cpf, senha):
    # Conexão com o banco de dados
    conn = sqlite3.connect('bemchique_db.db')
    cursor = conn.cursor()

    # Verificar as credenciais
    cursor.execute("SELECT * FROM usuarios WHERE email_cpf = ? AND senha = ?", (email_cpf, senha))
    usuario = cursor.fetchone()

    conn.close()
    return usuario


# Define a rota principal para o usuario
@app.route("/")
def home():
    categorias = ['Blusas', 'Camisetas', 'Moletons']
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
    return render_template('produtos.html')

# Define a rota para a página de Lista de Produtos
@app.route('/lista_produtos')
def lista_produtos():
    return render_template('lista-produtos.html')

# Define a rota para a página de Lista de Produtos Mais Vendidos
@app.route('/mais_vendidos')
def mais_vendidos():
    return render_template('mais-vendidos.html')

# Define a rota para a página de combos
@app.route('/combos')
def combos():
    return render_template('combos.html')

# Define a rota para a página Novidades
@app.route('/novidades')
def novidades():
    return render_template('novidades.html')

# Define a rota para a página Sistemas
@app.route('/sistemas')
def sistemas():
    title='Login'
    return render_template('sistema/index.html', title=title, nome_loja=nome_loja)

# Define a rota para a página de Categorias
@app.route('/categorias')
def categorias():
    return render_template('categorias.html')

# Define a rota para a página de Promoções
@app.route('/promotions')
def promotions():
    return render_template('promocoes.html')

# Define a rota para a página Contatos
@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

# Define a rota para a página Sobre
@app.route('/sobre')
def sobre():
    return render_template('about.html')

# Define a rota par a página Carrinhos
@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

# Define a rota para a página Blog
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Define a rota para a página de Autenticação
@app.route('/autenticar', methods=["GET","POST"])
def autenticar():
    try:
        email_cpf = request.form['email_cpf']
        senha = request.form['senha']
        
        usuario = verificar_credenciais(email_cpf, senha)

        return f'Autenticação bem-sucedida!'
    except Exception as e:
        return f'Erro: {e}'

    return 'Método não é válido para esta rota.'

# Define a rota para a página de Cadastro
@app.route('/cadastrar', methods=["POST", "GET"])
def cadastrar():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        senha = request.form['senha']
        senha_cripto = request['confirma_senha']
        print(nome, email, cpf, senha, senha_cripto)


    return redirect(url_for('home'))

with app.app_context():
    #Cria o banco de dados
    db.create_all()

if __name__ == '__main__':
    
    # Inicia o servidor flask
    app.run(debug=True)