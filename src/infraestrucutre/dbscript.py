from infraestrucutre.models import *


class PopulateDB:
    def __init__(self, db):
        self.db = db

    def populate(self,):
        self.db.session.add(UserType(id=1, name='Client'))
        self.db.session.add(UserType(id=2, name='Provider'))
        self.db.session.commit()
        
        self.db.session.add(Services(id=1, name='Reparo'))
        self.db.session.add(Services(id=2, name='Construção'))
        self.db.session.add(Services(id=3, name='Marcenaria'))
        self.db.session.add(Services(id=4, name='Pintura'))
        self.db.session.add(Services(id=5, name='Eletricista'))
        self.db.session.add(Services(id=6, name='Encanamento'))
        self.db.session.add(Services(id=7, name='Jardinagem'))
        self.db.session.add(Services(id=8, name='Limpeza'))
        self.db.session.add(Services(id=9, name='Enfermagem'))
        self.db.session.add(Services(id=10, name='Saúde'))
        self.db.session.add(Services(id=11, name='Beleza'))
        self.db.session.add(Services(id=12, name='Assistência Técnica'))
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
        self.db.session.add(Status(id=1, name='Solicitado', descricao='Solicitado ao executor do trabalho'))
        self.db.session.add(Status(id=2, name='Orçado', descricao='Recebido o orçamento do serviço'))
        self.db.session.add(Status(id=3, name='Orçamento Aceito', descricao='Orçamento aceito pelo contratante do serviço'))
        self.db.session.add(Status(id=4, name='Rejeitado Pelo Prestador', descricao='Trabalho negado pelo prestador do serviço'))
        self.db.session.add(Status(id=5, name='A ser executado', descricao='Aguardando realização do trabalho'))
        self.db.session.add(Status(id=6, name='Reaberto', descricao='Solicitação reaberta'))
        self.db.session.add(Status(id=7, name='Finalizado pelo prestador', descricao='Finalizado pelo prestador'))
        self.db.session.add(Status(id=8, name='Finalizado pelo cliente', descricao='Finalizado pelo cliente'))
        self.db.session.add(Status(id=9, name='Finalizado', descricao='Finalizado pelos cliente e prestador'))
        self.db.session.commit()