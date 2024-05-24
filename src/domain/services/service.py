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

    def verify_user_provider_service(self, user:int, service:int):
        userServices = self.repositories.get_user_service_by_user(user)
        for userServices in userServices:
            if userServices.service_id == service:
                return True
        return False

    def isTheServicePossibleToBeGenerated(self, client:int, provider:int, service:int):
        provider = self.repositories.get_user_by_id(provider)
        if provider.user_type != 2:
            raise ValueError('Usuário não é um prestador de serviço')
        if not self.verify_user_provider_service(provider.id, service):
            raise ValueError('Usuário não é prestador do serviço')
        serviceOrders = self.repositories.get_services_order_by_client_provider(client, provider.id)
        for serviceOrder in serviceOrders:
            if serviceOrder.service==service and serviceOrder.status in [1, 2, 3, 5, 6]:
                raise ValueError('Serviço já solicitado')
        return True

    def request_service_order(self, client:int, provider:int, service:int):
        try:
            if self.isTheServicePossibleToBeGenerated(client, provider, service):
                serviceOrder = self.repositories.create_service_order(
                    client_id=client, 
                    provider_id=provider, 
                    service_id=service, 
                    solicitation_date=datetime.now(),
                    status=1
                )
                serviceOrder = {
                    'client': serviceOrder.service_client,
                    'provider': serviceOrder.service_provider,
                    'service': serviceOrder.service,
                    'solicitation_date': serviceOrder.solicitation_date,
                    'status': serviceOrder.status
                }
                return serviceOrder
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