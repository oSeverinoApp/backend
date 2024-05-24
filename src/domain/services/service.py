from domain.ports.repositories import RepositoriesInterface
from domain.entities import User
from datetime import datetime
## Aqui fica a regra de negócio do sistema
#API deve chamar o service e o service chamar o repository, o repository chama o ORM e o ORM chama o banco de dados
#O service é o responsável por orquestrar as chamadas entre a API e o ORM
# A classe Service deve ser quebrada em varias classes, cada uma com sua responsabilidade
class Service:
    def __init__(self, repositories: RepositoriesInterface):
        self.repositories = repositories

    def create_user(self, name, email, state, city):
        user = User(name, email, state, city, user_type=1)
        try:
            user = self.repositories.create_user(user)
            return {
                'name': user.name,
                'email': user.email,
                'state': user.state,
                'city': user.city
            }
        except ValueError as e:
            raise ValueError(f'Erro ao criar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')


    def get_user_by_email(self, email:str):
        try:
            user = self.repositories.get_user_by_email(email)
            return user
        except ValueError as e:
            raise ValueError(f'Erro ao buscar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
        
    def get_users_by_city(self, city:str):
        return self.repositories.get_users_by_city(city)
    
    def get_users_by_state(self, state:str):
        return self.repositories.get_users_by_state(state)
    
    def add_user_service(self, user:User, service:int):
        pass

    def get_user_services_by_user(self, user:int):
        pass

    def remove_user_service_from_user(self, user:int, service:int):
        pass

    def create_service_order(self, client:int, provider:int, service:int, status:int, solicitation_date:datetime):
        pass