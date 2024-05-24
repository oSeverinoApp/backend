from adapters.sqlalchemyrepositories import SqlAchemyRepositories
from domain.entities import User
from datetime import datetime
## Aqui fica a regra de negócio do sistema
#API deve chamar o service e o service chamar o repository, o repository chama o ORM e o ORM chama o banco de dados
#O service é o responsável por orquestrar as chamadas entre a API e o ORM
# A classe Service deve ser quebrada em varias classes, cada uma com sua responsabilidade
class Service:
    def __init__(self, repositories: SqlAchemyRepositories):
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
        try:
            users = self.repositories.get_users_by_city(city)
            return users
        except ValueError as e:
            raise ValueError(f'Erro ao buscar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
    
    def get_users_by_state(self, state:str):
        try:
            users = self.repositories.get_users_by_state(state)
            return users
        except ValueError as e:
            raise ValueError(f'Erro ao buscar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
    
    def add_user_service(self, user:int, service:int):
        try:
            return self.repositories.add_user_service(user, service)
        except ValueError as e:
            raise ValueError(f'Erro ao adicionar serviço ao usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')

    def get_users_by_service(self, service:str):
        try:
            users = self.repositories.get_users_by_service(service)
            return users
        except ValueError as e:
            raise ValueError(f'Erro ao buscar usuario: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')

    def request_service_order(self, client:int, provider:int, service:int):
        try:
            return self.repositories.create_service_order(
                client_id=client, 
                provider_id=provider, 
                service_id=service, 
                solicitation_date=datetime.now(),
                status=1
            )
        except ValueError as e:
            raise ValueError(f'Erro ao solicitar serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
        
    def reject_service_order(self, service_order:int):
        try:
            return self.repositories.reject_service_order(
                service_order=service_order,
                status=4
            )
        except ValueError as e:
            raise ValueError(f'Erro ao rejeitar serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
    
    def send_service_order_value(self, service_order:int, value:float):
        try:
            return self.repositories.send_service_order_value(
                service_order=service_order, 
                value=value,
                status=2
            )
        except ValueError as e:
            raise ValueError(f'Erro ao enviar valor do serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
        
    def accept_service_order_value(self, service_order:int):
        try:
            return self.repositories.accept_service_order_value(
                service_order=service_order,
                status=3
            )
        except ValueError as e:
            raise ValueError(f'Erro ao aceitar valor do serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
        
    def reject_service_order_value(self, service_order:int):
        try:
            return self.repositories.reject_service_order_value(
                service_order,
                status=12
            )
        except ValueError as e:
            raise ValueError(f'Erro ao rejeitar valor do serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')
        
    def finish_service_order_by_client(self, service_order:int, rating:int, comment:str):
        try:
            return self.repositories.finish_service_order(
                service_order, 
                status=8,
                rating=rating,
                comment=comment
            )
        except ValueError as e:
            raise ValueError(f'Erro ao finalizar serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')

    def finish_service_order_by_provider(self, service_order:int):
        try:
            return self.repositories.finish_service_order(
                service_order,
                status=7
            )
        except ValueError as e:
            raise ValueError(f'Erro ao finalizar serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')    
        
    def reopen_service_order(self, service_order:int):
        try:
            return self.repositories.reopen_service_order(
                service_order,
                status=6
            )
        except ValueError as e:
            raise ValueError(f'Erro ao reabrir serviço: {str(e)}')
        except Exception as e:
            print(str(e))
            raise Exception('Internal server error')