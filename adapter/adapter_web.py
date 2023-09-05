# adapter_web

from flask import Flask, request, render_template
from app import carrinho, catalogo, pedidos

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    render_template('index.html')

@app.route('/carrinho', methods=['POST'])
def adicionar_ao_carrinho():
    render_template('carrinho.html')

@app.route('/catalogo', methods=['GET'])
def listar_produtos():
    render_template('catalogo.html')