from flask import Blueprint

bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates/sistemas/templates")

@bp_usuarios.route('/create')
def create():
    return render_template('usuarios_create.html')
