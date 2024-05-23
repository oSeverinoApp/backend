# infraestrutura/modelos.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
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
    user_type = Column(Integer, ForeignKey('user_type.id'))
    password = Column(String)
    access_token = Column(String)


class ServicesTable(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class UserServicesTable(Base): 
    __tablename__ = 'user_services'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))


class UserTypeTable(Base):
    __tablename__ = 'user_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)


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
    value = Column(Float)

class StatusTable(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    name = Column(String)
