from flask import Flask, abort, render_template, redirect, flash, request, send_file, send_from_directory, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from models import db, User
from sqlalchemy import inspect
import time
import config
import sqlite3
import config
import secrets

app = Flask(__name__)

app.config['SESSION_TYPE'] = config.SESSION_TYPE
app.config['SESSION_PERMANENT'] = config.SESSION_PERMANENT
app.config['SESSION_USER_SIGNER'] = config.SESSION_USER_SIGNER
app.config['SESSION_KEY_PREFIX'] = config.SECRET_KEY
app.config['DEBUG'] = config.DEBUG
app.config['SECRET_KEY'] = config.SECRET_KEY 
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

Session(app)

# Define a rota principal para o usuario
@app.route("/")
def home():
    categorias = ['Blusas', 'Camisetas', 'Moletons']
    return render_template(
        "index.html", 
        categorias=categorias,
        title='Showcase',
        endereco_loja=config.endereco_loja,
        texto_destaque=config.texto_destaque,
        whatsapp=config.whatsapp,
        nome_loja=config.nome_loja,
        whatsapp_link=config.whatsapp_link,
        email=config.email,
        telefone=config.telefone,
        instagram_link=config.instagram_link
        )

# Define a rota para a página Sistemas
@app.route('/sistema', methods=['GET', 'POST'])
def sistemas():
   
    if request.method == 'POST':
          
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not email or not senha : # Verifica se o existe email ou senha
            flash('Informe o email e a senha.','warning')
        
        user = User.query.filter_by(email=email, senha=senha).first()
        
        if user:
            
            session['user_id'] = user.id
            if user.profile == 'admin':
                return redirect(url_for('painel_admin', admin=user.id))
            elif user.profile == 'user':
                return redirect(url_for('painel_client', user=user.id))
        else:
            flash('Credenciais inválidas','danger')
    
    title ='Login'
    texto_destaque = config.texto_destaque
    email = config.email
    
    return render_template('sistema/index.html', title=title, email=email, texto_destaque=texto_destaque)

# Define a rota para a página de Cadastro
@app.route('/sistema/register', methods=["POST", "GET"])
def register():
    email = config.email
    texto_destaque = config.texto_destaque
    title = 'Novo Usuário'
    if request.method == "POST":
        nome = request.form['name']
        username = request.form['username']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['confirma-senha']
        active = True
        perfil ='user'
        
        novo_usuario = User(name=nome, email=email, username=username, senha=senha, ativo=active, profile=perfil)
        
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            dados = flash('Usuário registrado com sucesso','success')
        except Exception as e:
            
            db.session.rollback() # Desfaz a transação que causou o erro
            title = 'Register Error'
            dados = ''
            flash("Este usuário ja existe no sistema.","warning")
            time.sleep(5) # Adiciona um atraso de 5 segundos

            return render_template("sistema/autenticar_user.html", title=title, email=email, dados=dados, texto_destaque=texto_destaque)
            
    
    return render_template("sistema/register_user.html", title=title, email=email, texto_destaque=texto_destaque)


# Define a rota para o painel de cliente
@app.route('/sistema/painel/dashboard/<user>', methods=["GET","POST"])
def painel_client(user):
    if 'user_id' not in session or session['user_id'] != int(user): # Verifica se há uma sessão ativa e se o usuário é o correto
        print(f"session['user_id']: {session.get('user_id')}")
        print(session)
        print(f"user from URL: {user}")
        abort(403) # Acesso negado
    
    title = 'Cliente'
    email = config.email
    dados = f'Aqui é painel do {title}.'
    return render_template('/sistema/painel-client/index.html', title=title, email=email, dados=dados)

# Define a rota para o painel de administrador
@app.route('/sistema/painel/manager/<admin>', methods=["GET","POST"])
def painel_admin(admin):
    
    if 'user_id' not in session or session['user_id'] != int(admin):  # Verifica se há uma sessão ativa e se o usuário é o correto
        print(f"session['user_id']: {session.get('user_id')}")
        print(f"admin from URL: {admin}")
        abort(403)  # Acesso não autorizado

    user = User.query.get(int(admin))
    if user and user.profile != 'admin': # Obtem o objeto User do banco de dados pelo ID
        abort(403) # Acesso não autorizado se o usuário não for um Administrador
    
    title = 'Administrador'
    email = config.email
    dados = f'Aqui é o Painel do {title}'
    return render_template('/sistema/painel-admin/index.html', title=title, email=email, dados=dados)
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


if __name__ == '__main__':

    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table("user"):
            db.create_all()
    app.run(debug=True)
    