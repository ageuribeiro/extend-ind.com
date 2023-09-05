import secrets
import pytz
from datetime import datetime

def convert_to_timezone(dt, timezone):
    source_timezone = pytz.timezone('UTC')  # Fuso horário de origem (pode variar)
    target_timezone = pytz.timezone(timezone)  # Fuso horário de destino
    localized_dt = source_timezone.localize(dt)
    target_dt = localized_dt.astimezone(target_timezone)
    return target_dt

    
# VARIÁVEIS GLOBAIS
email = 'bemchiquemodaelegante@gmail.com'
whatsapp_link ='5511977523331'
telefone = '+55 (11) 97752-3331'
whatsapp ='+55 (11) 97752-3331'
instagram_link = 'https://www.instagram.com/bemchiques/'
nome_loja = 'Boutique Bem Chique'
texto_destaque = 'Produtos em Destaque!'
endereco_loja = 'www.bemchique.com.br'

# VARIÁVEIS DE AMBIENTE
DEBUG = True
SECRET_KEY = secrets.token_hex(16)
DATABASE_URI = 'sqlite:///database.db'

# VARIÁVEIS DE SESSÃO
SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = False
SESSION_USER_SIGNER = True

# VARIAVEIS DO ADMINISTRADOR
ADMIN_USERNAME = 'rayssasoares'
ADMIN_NAME = 'Rayssa Soares'
ADMIN_EMAIL = 'rayssanogueira2023@gmail.com'
ADMIN_PASSWORD = 'bemchique2023'

# VARIAVEIS DE BANCP DE DADOS
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False