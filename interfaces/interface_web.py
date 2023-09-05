# interface_web.py

from flask import Flask
from adapter import adapter_web

app = Flask(__name__)

app.register_blueprint(adapter_web)