# infraestrutura/modelos.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    city = Column(String)
    state = Column(String)
    user_type = Column(Integer, ForeignKey('user_types.id'))
    password = Column(String)
    access_token = Column(String)
    user_services = relationship("UserServicesTable", back_populates="user")
    user_type = relationship("UserTypeTable", back_populates="users")


class ServicesTable(Base):
    
    #Marcenaria
    #Pintura
    #Eletricista
    #Encanamento
    #Jardinagem
    #Limpeza
    #Enfermagem
    #Saúde
    #Beleza
    #Assistência Técnica
    
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_services = relationship("UserServicesTable", back_populates="services")


class UserServicesTable(Base): 
    __tablename__ = 'user_services'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    user = relationship("UserTable", back_populates="user_services")
    services = relationship("ServicesTable", back_populates="user_services")



class UserTypeTable(Base):
    __tablename__ = 'user_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship("UserTable", back_populates="user_type")


class ServiceOrder(Base):
    __tablename__ = 'service_orders'

    id = Column(Integer, primary_key=True)
    service_client = Column(Integer, ForeignKey('users.id'))
    service_provider = Column(Integer, ForeignKey('users.id'))
    service = Column(Integer, ForeignKey('services.id'))
    status = Column(Integer, ForeignKey('status.id'))
    solicitation_date = Column(DateTime)
    service_conclusion_date = Column(DateTime)
    service_rating = Column(Integer)
    service_comment = Column(String)
    service = relationship("ServicesTable", back_populates="service_orders")
    status = relationship("StatusTable", back_populates="service_orders")

class StatusTable(Base):
    __tablename__ = 'status'
    #open cliente solicita serviço
    #provider_accept prestador aceita devolvendo orçamento
    #client_accept cliente aceita orçamento
    #provider_reject prestador rejeita o pedido
    #waiting_progress serviço em andamento
    #reopen cliente reabre
    #provider_finished serviço finalizado pelo prestador
    #client_finished serviço finalizado pelo cliente
    #close serviço finalizado

    id = Column(Integer, primary_key=True)
    name = Column(String)
    service_orders = relationship("ServiceOrder", back_populates="status")
    

"""
Marcenaria
Pintura
Eletricista
Encanamento
Jardinagem
Limpeza
Enfermagem
Saúde
Beleza
Assistência Técnica
"""

