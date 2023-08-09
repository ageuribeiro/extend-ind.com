import config
import sqlite3
from time_utils import convert_to_timezone
import pytz
from datetime import datetime

try:
    conexao = sqlite3.connect(config.banco)
    print('A conexão com o banco de dados foi estabelecida.')
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)