from infraestrucutre.models import *


class PopulateDB:
    def __init__(self, db):
        self.db = db

    def populate(self,):
        self.db.session.add(UserTypeTable(name='Client'))
        self.db.session.add(UserTypeTable(name='Provider'))
        self.db.session.commit()
        
        self.db.session.add(ServicesTable(name='Reparo'))
        self.db.session.add(ServicesTable(name='Construção'))
        self.db.session.add(ServicesTable(name='Marcenaria'))
        self.db.session.add(ServicesTable(name='Pintura'))
        self.db.session.add(ServicesTable(name='Eletricista'))
        self.db.session.add(ServicesTable(name='Encanamento'))
        self.db.session.add(ServicesTable(name='Jardinagem'))
        self.db.session.add(ServicesTable(name='Limpeza'))
        self.db.session.add(ServicesTable(name='Enfermagem'))
        self.db.session.add(ServicesTable(name='Saúde'))
        self.db.session.add(ServicesTable(name='Beleza'))
        self.db.session.add(ServicesTable(name='Assistência Técnica'))
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
        self.db.session.add(StatusTable(name='Solicitado'))
        self.db.session.add(StatusTable(name='Orçado'))
        self.db.session.add(StatusTable(name='Orçamento Aceito'))
        self.db.session.add(StatusTable(name='Rejeitado Pelo Prestador'))
        self.db.session.add(StatusTable(name='A ser executado'))
        self.db.session.add(StatusTable(name='Reaberto'))
        self.db.session.add(StatusTable(name='Finalizado pelo prestador'))
        self.db.session.add(StatusTable(name='Finalizado pelo cliente'))
        self.db.session.add(StatusTable(name='Finalizado'))
        self.db.session.commit()