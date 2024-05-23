class User:
    def __init__(self, id: int, name: str, email: str, cidade: str, estado: str, tipo: str):
        self.id = id
        self.name = name
        self.email = email
        self.cidade = cidade
        self.estado = estado
        self.user_type = tipo
        
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

class Services:
    def __init__(self, id: int, name: str, descricao: str, user_id: int):
        self.id = id
        self.name = name
        self.descricao = descricao
        self.user_id = user_id

    def __repr__(self):
        return f"<Services(name='{self.name}', descricao='{self.descricao}')>"