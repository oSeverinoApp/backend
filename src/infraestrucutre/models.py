# infraestrutura/modelos.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from infraestrucutre.db_setup import db

class Users(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    user_type = db.Column(db.Integer, ForeignKey('user_type.id'))
    password = db.Column(db.String(255))
    access_token = db.Column(db.String(1024))


class Services(db.Model):
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

class UserServices(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    service_id = db.Column(db.Integer, ForeignKey('services.id'))

class UserType(db.Model):
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

class ServiceOrder(db.Model):
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_client = db.Column(db.Integer, ForeignKey('users.id'))
    service_provider = db.Column(db.Integer, ForeignKey('users.id'))
    service = db.Column(db.Integer, ForeignKey('services.id'))
    status = db.Column(db.Integer, ForeignKey('status.id'))
    solicitation_date = db.Column(db.DateTime)
    service_conclusion_date = db.Column(db.DateTime)
    service_rating = db.Column(db.Integer)
    service_comment = db.Column(db.String(255))
    value = db.Column(db.Float)

class Status(db.Model):        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    descricao = db.Column(db.String(255))
