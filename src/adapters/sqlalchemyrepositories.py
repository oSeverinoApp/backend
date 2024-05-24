from domain.ports.repositories import RepositoriesInterface
from infraestructure.models import Users, UserServices, ServiceOrder, Services
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

    def get_user_by_id(self, id:int):
        user = self.db.session.query(Users).filter_by(id=id).first()
        if user:
            return user
        return None
    
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
    
    def add_user_service(self, user_id:int, service_id:int):
        userServices = UserServices(user_id=int(user_id), service_id=int(service_id))
        self.db.session.add(userServices)
        self.db.session.commit()
        return userServices
    def get_user_services(self, user_id:int):
        userServices = self.db.session.query(UserServices).filter_by(user_id=user_id).all()
        return userServices
    
    def get_service_by_user(self, user:int):
        services = self.db.session.query(Services).join(UserServices, Services.id==UserServices.service_id).filter(UserServices.user_id==user).all()
        return services

    def get_users_by_service(self, service:int):
        users = self.db.session.query(Users).join(UserServices, Users.id==UserServices.user_id).filter(UserServices.service_id==service).all()
        return [User(user.name, user.email, user.state, user.city) for user in users]
    
    def create_service_order(self,
                                client_id:int,
                                provider_id:int,
                                service_id:int,
                                solicitation_date:datetime,
                                status:int,
                            ):
        serviceOrder = ServiceOrder(service_client=client_id, 
                     service_provider=provider_id, 
                     service=service_id, 
                     solicitation_date=solicitation_date, 
                     status=status
        )
        self.db.session.add(serviceOrder)
        self.db.session.commit()
        return serviceOrder
    

    def reject_service_order(self,
                                service_order_id:int,
                                status:int,
                            ):
        serviceOrder = ServiceOrder.query.filter_by(id=service_order_id).first()
        serviceOrder.status = status
        self.db.session.commit()
        return serviceOrder

    def send_service_order_value(self,
                                service_order_id:int,
                                value:float,
                                status:int,
                            ):
        serviceOrder = ServiceOrder.query.filter_by(id=service_order_id).first()
        serviceOrder.value = value
        serviceOrder.status = status
        self.db.session.commit()
        return serviceOrder

    def accept_service_order_value(self,
                                service_order_id:int,
                                status:int,
                            ):
        serviceOrder = ServiceOrder.query.filter_by(id=service_order_id).first()
        serviceOrder.status = status
        self.db.session.commit()
        return serviceOrder

    def reject_service_order_value(self,
                                service_order_id:int,
                                status:int,
                            ):
        serviceOrder = ServiceOrder.query.filter_by(id=service_order_id).first()
        serviceOrder.status = status
        self.db.session.commit()
        return serviceOrder

    def finish_service_order(self,
                                service_order_id:int,
                                status:int,
                                rating:int,
                                comment:str,
                                service_conclusion_date:datetime = None,
                            ):
        serviceOrder = ServiceOrder.query.filter_by(id=service_order_id).first()
        serviceOrder.status = status
        serviceOrder.service_rating = rating
        serviceOrder.service_comment = comment
        serviceOrder.service_conclusion_date = service_conclusion_date
        self.db.session.commit()
        return serviceOrder

    def reopen_service_order(self,
                                service_order_id:int,
                                status:int,
                            ):
        serviceOrder = ServiceOrder.query.filter_by(id=service_order_id).first()
        serviceOrder.status = status
        self.db.session.commit()
        return serviceOrder
    
