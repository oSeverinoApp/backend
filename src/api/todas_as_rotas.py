from flask import Flask, jsonify, request, Blueprint
from adapters.sqlalchemyrepositories import SqlAchemyRepositories
from domain.services.service import Service
from infraestrucutre.db_setup import db
from infraestrucutre.dbscript import PopulateDB

repositories = SqlAchemyRepositories(db=db)
domainService = Service(repositories)

populateDB = PopulateDB(db=db)

rotas_controller = Blueprint('api', __name__)

@rotas_controller.route("/teste", methods=['GET'])
def teste():
    return jsonify({'message': 'Teste'})

@rotas_controller.route('/populate_db', methods=['GET'])
def populate_db():
    try:
        populateDB.populate()
        return jsonify({'message': 'Database populated successfully'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500

@rotas_controller.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        domainService.create_user(data['name'], data['email'], data['state'], data['city'])
        return jsonify({'message': 'User created successfully'})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500