import secrets

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