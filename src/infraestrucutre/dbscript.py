from infraestrucutre.models import *


class PopulateDB:
    def __init__(self, db):
        self.db = db

    def populate(self,):
        user_types = [
            UserType(id=1, name='Client'),
            UserType(id=2, name='Provider')
        ]
        for user_type in user_types:
            try:
                self.db.session.add(user_type)
                self.db.session.commit()
            except:
                self.db.session.rollback()
                print("User Type {} já cadastrado".format(user_type.name))

        services = [
            Services(id=1, name='Reparo'),
            Services(id=2, name='Construção'),
            Services(id=3, name='Marcenaria'),
            Services(id=4, name='Pintura'),
            Services(id=5, name='Eletricista'),
            Services(id=6, name='Encanamento'),
            Services(id=7, name='Jardinagem'),
            Services(id=8, name='Limpeza'),
            Services(id=9, name='Enfermagem'),
            Services(id=10, name='Saúde'),
            Services(id=11, name='Beleza'),
            Services(id=12, name='Assistência Técnica')
        ]
        for service in services:
            try:
                self.db.session.add(service)
                self.db.session.commit()
            except:
                self.db.session.rollback()
                print("Serviço {} já cadastrado".format(service.name))

        statuses = [
            Status(id=1, name='Solicitado', descricao='Solicitado ao executor do trabalho'),
            Status(id=2, name='Orçado', descricao='Prestador propoe o orçamento do serviço'),
            Status(id=3, name='Orçamento Aceito', descricao='Orçamento aceito pelo contratante do serviço'),
            Status(id=4, name='Rejeitado Pelo Prestador', descricao='Trabalho negado pelo prestador do serviço'),
            Status(id=5, name='A ser executado', descricao='Aguardando realização do trabalho'),
            Status(id=6, name='Reaberto', descricao='Solicitação reaberta'),
            Status(id=7, name='Finalizado pelo prestador', descricao='Finalizado pelo prestador'),
            Status(id=8, name='Finalizado pelo cliente', descricao='Finalizado pelo cliente'),
            Status(id=9, name='Finalizado', descricao='Finalizado pelos cliente e prestador'),
            Status(id=10, name='Cancelado', descricao='Cancelado pelo cliente'),
            Status(id=11, name='Cancelado pelo prestador', descricao='Cancelado pelo prestador'),
            Status(id=12, name='Orçamento rejeitado', descricao='Orçamento rejeitado pelo cliente')
        ]
        for status in statuses:
            try:
                self.db.session.add(status)
                self.db.session.commit()
            except:
                self.db.session.rollback()
                print("Status {} já cadastrado".format(status.name))

        users = [
            Users(name='Joao', email="teste1@teste1.com", city="Belo Horizonte", state="MG", user_type=1),
            Users(name='Maria', email="teste2@teste1.com", city="Belo Horizonte", state="MG", user_type=2),
            Users(name='Jose', email="jose@trabalahdor.com", city="Contagem", state="MG", user_type=2),
            Users(name='Pedro', email="pedro@email.com", city="Contagem", state="MG", user_type=2),
            Users(name='Luciana', email="luciana@lu.com", city="Belo Horizonte", state="MG", user_type=2),
            Users(name='Marcia', email="marcio@lu.com", city="Belo Horizonte", state="MG", user_type=2),
            Users(name='Marcos', email="marcos@lu.com", city="Belo Horizonte", state="MG", user_type=2),
            Users(name='Douglas', email="doug@lu.com", city="Belo Horizonte", state="MG", user_type=2),
            Users(name='Juliana', email="juliana@lu.com", city="Belo Horizonte", state="MG", user_type=2),
            Users(name='Matias', email="matias@lu.com", city="Belo Horizonte", state="MG", user_type=2),
            Users(name='Juriema', email="juriema@lu.com", city="Belo Horizonte", state="MG", user_type=2)
        ]
        for user in users:
            try:
                self.db.session.add(user)
                self.db.session.commit()
            except:
                self.db.session.rollback()
                print("User {} já cadastrado".format(user.name))

        user_services = [
            UserServices(user_id=2, service_id=1),
            UserServices(user_id=3, service_id=2),
            UserServices(user_id=4, service_id=3),
            UserServices(user_id=5, service_id=4),
            UserServices(user_id=6, service_id=5),
            UserServices(user_id=7, service_id=6),
            UserServices(user_id=8, service_id=7),
            UserServices(user_id=9, service_id=8),
            UserServices(user_id=10, service_id=9),
            UserServices(user_id=11, service_id=10),
            UserServices(user_id=3, service_id=1),
            UserServices(user_id=4, service_id=1),
            UserServices(user_id=5, service_id=1),
            UserServices(user_id=6, service_id=1),
            UserServices(user_id=7, service_id=1),
            UserServices(user_id=8, service_id=1),
            UserServices(user_id=9, service_id=1),
        ]
        for user_service in user_services:
            try:
                self.db.session.add(user_service)
                self.db.session.commit()
            except Exception as e:
                self.db.session.rollback()
                print(e)
                print("User Service {} já cadastrado".format(user_service.id))
            