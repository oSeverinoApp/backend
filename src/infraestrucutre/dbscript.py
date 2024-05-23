from infraestrucutre.models import *


class PopulateDB:
    def __init__(self, db):
        self.db = db

    def populate(self,):
        self.db.session.add(UserType(name='Client'))
        self.db.session.add(UserType(name='Provider'))
        self.db.session.commit()
        
        self.db.session.add(Services(name='Reparo'))
        self.db.session.add(Services(name='Construção'))
        self.db.session.add(Services(name='Marcenaria'))
        self.db.session.add(Services(name='Pintura'))
        self.db.session.add(Services(name='Eletricista'))
        self.db.session.add(Services(name='Encanamento'))
        self.db.session.add(Services(name='Jardinagem'))
        self.db.session.add(Services(name='Limpeza'))
        self.db.session.add(Services(name='Enfermagem'))
        self.db.session.add(Services(name='Saúde'))
        self.db.session.add(Services(name='Beleza'))
        self.db.session.add(Services(name='Assistência Técnica'))
        self.db.session.commit()
        #open cliente solicita serviço
            #provider_accept prestador aceita devolvendo orçamento
            #client_accept cliente aceita orçamento
            #provider_reject prestador rejeita o pedido
            #waiting_progress em andamento
            #reopen cliente reabre
            #provider_finished finalizado pelo prestador
            #client_finished finalizado pelo cliente
            #close finalizado
        self.db.session.add(Status(name='Solicitado'))
        self.db.session.add(Status(name='Orçado'))
        self.db.session.add(Status(name='Orçamento Aceito'))
        self.db.session.add(Status(name='Rejeitado Pelo Prestador'))
        self.db.session.add(Status(name='A ser executado'))
        self.db.session.add(Status(name='Reaberto'))
        self.db.session.add(Status(name='Finalizado pelo prestador'))
        self.db.session.add(Status(name='Finalizado pelo cliente'))
        self.db.session.add(Status(name='Finalizado'))
        self.db.session.commit()