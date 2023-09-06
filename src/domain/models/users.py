class Users:
    def __init__(self, id: int, name: str, username: str, senha: str, profile: str, ativo: str)-> None:
        self.id = id
        self.name = name
        self.username = username
        self.senha = senha
        self.profile = profile
        self.ativo = ativo