from abc import ABC, abstractmethod

## Interface for Repositories
# Aqui é implementada a interface para o repositorio, interfaces sevem para abstrair a implementação do ReositorioORM
# O repositorio é implementado no arquivo adapters.repositories.py
# Aqui ficariam todas as funções que devem ser implementadas pelo RepositorioORM
# Isso seria uma superclasse e com o nome ruim, deve extrair os metodos dessa classe de forma a criar mais classes
# isso pqe esse repositorio tem os metodos de todas as classes
class RepositoriesInterface(ABC):
    def __init__(self):
        pass
    
    #Funções que deveriam estar numa classe de UserRepositoryInterface
    @abstractmethod
    def create_user():
        pass

    @abstractmethod
    def get_user_by_email():
        pass

    @abstractmethod
    def get_users_by_city():
        pass

    @abstractmethod
    def get_users_by_state():
        pass