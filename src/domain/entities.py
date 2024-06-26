class User:
    def __init__(self, name: str, email: str, state: str, city: str, user_type:int=1, id: int=None):
        self.id = id
        self.name = name
        self.email = email
        self.city = city
        self.state = state
        self.user_type = user_type
        
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