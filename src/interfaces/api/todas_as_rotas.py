from flask import Flask, jsonify, request, Blueprint
from app import app

rotas_controller = Blueprint('api', __name__)
class Rotas:
    def __init__(self,):
        self.app = app
    @app.route('/create_user', methods=['POST'])
    def create_user():
        ## criar usuario
        pass

    @app.route('/get_user', methods=['GET'])
    def get_user():
        ## pegar usuario
        pass

    @app.route('/update_user', methods=['PUT'])
    def update_user():
        ## atualizar usuario
        pass

    @app.route('/delete_user', methods=['DELETE'])
    def delete_user():
        ## deletar usuario
        pass

    @app.route("/list_users_by_name/<name>", methods=['GET'])
    def list_users_by_name(name):
        ## listar usuarios por nome
        pass

    @app.route("/list_services", methods=['GET'])
    def list_services():
        ## listar serviços
        pass
