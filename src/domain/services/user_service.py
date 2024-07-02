from adapters.sqlalchemyrepositories import SqlAchemyRepositories
from domain.entities import User
from datetime import datetime
## Aqui fica a regra de negócio do sistema
#API deve chamar o service e o service chamar o repository, o repository chama o ORM e o ORM chama o banco de dados
#O service é o responsável por orquestrar as chamadas entre a API e o ORM
# A classe Service deve ser quebrada em varias classes, cada uma com sua responsabilidade
class UserService:
    def __init__(self, repositories: SqlAchemyRepositories):
        self.repositories = repositories

    def create_user(self, name, email, state, city, user_type=1):
        ## Cria usuario
        try:
            user = self.repositories.get_user_by_email(email)
            if user:
                raise ValueError('User already registered.')
            else:
                user = User(name, email, state, city, user_type)
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
        try:
            users = self.repositories.get_users_by_city(city)
            users = [{'name': user.name, 'email': user.email, 'state': user.state, 'city': user.city} for user in users]
            return users
        except ValueError as e:
            raise ValueError(f'Erro ao buscar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
    
    def get_users_by_state(self, state:str):
        try:
            users = self.repositories.get_users_by_state(state)
            users = [{'name': user.name, 'email': user.email, 'state': user.state, 'city': user.city} for user in users]
            return users
        except ValueError as e:
            raise ValueError(f'Erro ao buscar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
    
    def verify_service_already_registered(self, user: int, service: int):
        userServices = self.repositories.get_user_services(user)
        for user_service in userServices:
            if user_service.service_id == service:
                return True
        return False

    def add_user_service(self, user: int, service: int):
        try:
            if self.verify_service_already_registered(user, service):
                raise ValueError('Serviço já cadastrado para o usuário')
            userService = self.repositories.add_user_service(user, service)
            return {'user_id': userService.user_id, 'service_id': userService.service_id}
        except ValueError as e:
            raise ValueError(f'Erro ao adicionar serviço ao usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')


    def get_users_by_service(self, service:int):
        try:
            users = self.repositories.get_users_by_service(service)
            users = [{'name': user.name, 'email': user.email, 'state': user.state, 'city': user.city} for user in users]
            return users
        except ValueError as e:
            raise ValueError(f'Erro ao buscar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
        
