import config
from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='/interfaces/templates')
app.config.from_pyfile('config.py')
app.debug = True
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
 