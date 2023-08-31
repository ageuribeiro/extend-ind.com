from flask import Flask, abort, render_template, redirect, flash, request, send_file, send_from_directory, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from models import *
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
    
    username = None

    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            username = user.name

    
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
        instagram_link=config.instagram_link,
        username=username
        )

# Define a rota para a página Sistemas
@app.route('/sistema', methods=['GET', 'POST'])
def sistemas():
   
    if request.method == 'POST':
          
        email = request.form.get('login-email')
        senha = request.form.get('login-senha')

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


# Define a rota para a página de Logout
@app.route('/sistema/logout')
def logout():
    
    if 'user_id' in session:
        session.pop('user_id', None)
    title = 'Thank You'
    email = config.email
    return redirect(url_for('home'))

# Define a rota para a página de Cadastro
@app.route('/sistema/register', methods=['GET', 'POST'])
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
@app.route('/sistema/painel/dashboard/<user>', methods=['GET', 'POST'])
def painel_client(user):

    if 'user_id' not in session or session['user_id'] !=int(user):
        abort(403) # Acesso negado
    
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            username = user.name

    title = 'Cliente'
    email = config.email
    dados = f'Aqui é painel do {title}.'
    return render_template('/sistema/painel-client/index.html', title=title, email=email, dados=dados, username=username)

# Define a rota para o painel de administrador
@app.route('/sistema/painel/manager/<admin>', methods=['GET', 'POST'])
def painel_admin(admin):
    username = None
    
    if 'user_id' not in session or session['user_id'] != int(admin):  # Verifica se há uma sessão ativa e se o usuário é o correto
        abort(403)  # Acesso não autorizado

    if 'user_id' in session:
        user_id =session['user_id']
        user = User.query.get(user_id)
        if user:
            username = user.name
    
    title = 'Administrador'
    email = config.email
    return render_template('/sistema/painel-admin/index.html', title=title, email=email, username=username)
    
# Define a rota para página Produtos
@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    return render_template('produtos.html')

# Define a rota para a página de Lista de Produtos
@app.route('/lista_produtos', methods=['GET', 'POST'])
def lista_produtos():
    return render_template('lista-produtos.html')

# Define a rota para a página de Gerenciamento de Categorias
@app.route('/sistema/manager/categorias', methods=['GET', 'POST'])
def manager_categorias():
    return render_template('/sistema/categorias/index.html') 

# Define a rota para o modal de novos produtos
@app.route('/sistema/painel/manager/novo-produto')
def novo_produto():
    return render_template('/sistema/painel-admin/produto/novo_produto.html', conteudo_do_modal='Conteudo Dinâmico')

# Define a rota para a página de Lista de Produtos Mais Vendidos
@app.route('/mais_vendidos', methods=['GET', 'POST'])
def mais_vendidos():
    return render_template('mais-vendidos.html')

# Define a rota para a página de combos
@app.route('/combos', methods=['GET', 'POST'])
def combos():
    return render_template('combos.html')

# Define a rota para a página Novidades
@app.route('/novidades', methods=['GET', 'POST'])
def novidades():
    return render_template('novidades.html', methods=['GET', 'POST'])

# Define a rota para a página de Categorias
@app.route('/categorias' , methods=['GET', 'POST'])
def categorias():

    pag = categorias()
    menu = ["produtos","categorias","sub-categorias","combos","promocoes","clientes","vendas","backup"]
    username = None

    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            username = user.name

    return render_template('categorias.html', pag = pag, username = username, menu=menu)

# Define a rota para a página de Promoções
@app.route('/promotions', methods=['GET', 'POST'])
def promotions():
    return render_template('promocoes.html')

# Define a rota para a página Contatos
@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    title='Contatos'
    email = config.email
    telefone =  config.telefone
    return render_template('contatos.html', email=email, telefone=telefone, title=title)

# Define a rota para a página Sobre
@app.route('/sobre')
def sobre():
    title = 'Sobre'
    email = config.email
    telefone = config.telefone
    return render_template('about.html', title=title, email=email, telefone=telefone)

# Define a rota par a página Carrinhos
@app.route('/carrinho', methods=['GET', 'POST'])
def carrinho():
    return render_template('carrinho.html')

# Define a rota para a página Blog
@app.route('/blog', methods=['GET', 'POST'])
def blog():
    title = 'Blog'
    telefone = config.telefone
    email = config.email
    return render_template('blog.html', email=email, title=title, telefone=telefone)

with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table("User"):
        db.create_all()

    admin_username = config.ADMIN_USERNAME
    admin_exists = User.query.filter_by(username=admin_username, profile='admin').first()

    if not admin_exists:
        admin_user = User(
            name=config.ADMIN_NAME,
            email=config.ADMIN_EMAIL,
            username=admin_username,
            senha=config.ADMIN_PASSWORD,
            ativo=True,
            profile='admin'
        )

        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
    