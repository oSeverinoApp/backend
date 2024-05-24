from domain.ports.repositories import RepositoriesInterface
from infraestrucutre.models import Users
from domain.entities import User
from datetime import datetime
class SqlAchemyRepositories(RepositoriesInterface):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def create_user(self, user:User):
        user = Users(name=user.name, email=user.email, state=user.state, city=user.city, user_type=1)
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def get_user_by_email(self, email:str):
        user = self.db.session.query(Users).filter_by(email=email).first()
        if user:
            return user
        return None
    
    def get_users_by_city(self, city:str):
        users = self.db.session.query(Users).filter_by(city=city).all()
        return [User(user.name, user.email, user.state, user.city) for user in users]
    
    def get_users_by_state(self, state:str):
        users = self.db.session.query(Users).filter_by(state=state).all()
        return [User(user.name, user.email, user.state, user.city) for user in users]
    
    def add_user_service(self, user:int, service:int):
        pass
