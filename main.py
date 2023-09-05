# main.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__, template_folder='/interfaces/templates')
app.config.from_pyfile('config.py')
app.debug = True
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
 