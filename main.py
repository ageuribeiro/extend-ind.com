from flask import Flask
from infraestrutura.database import db

app = Flask(__name__)
app.config.from_pyfile('config.py')


# Inicializar o SQLAlchemy
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
 