from flask import Flask, jsonify, request, Blueprint
from adapters.sqlalchemyrepositories import SqlAchemyRepositories
from domain.services.service import Service
from infraestrucutre.db_setup import db
from infraestrucutre.dbscript import PopulateDB

repositories = SqlAchemyRepositories(db=db)
domainService = Service(repositories)

populateDB = PopulateDB(db=db)

rotas_controller = Blueprint('api', __name__)
#http://127.0.0.1/api/teste
@rotas_controller.route("/teste", methods=['GET'])
def teste():
    return jsonify({'message': 'Teste'})

@rotas_controller.route('/populate_db', methods=['GET'])
def populate_db():
    try:
        populateDB.populate()
        return jsonify({'message': 'Database populated successfully',})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500

@rotas_controller.route('/create_user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        data = domainService.create_user(data['name'], data['email'], data['state'], data['city'])
        return jsonify({'message': 'User created successfully',
                        "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500
    
#http://127.0.0.1:5000/api/get_user_by_email/teste@asd.com
@rotas_controller.route('/get_user_by_email/<email>', methods=['GET'])
def get_user_by_email(email):
    try:
        user = domainService.get_user_by_email(email)
        if user:
            return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'state': user.state, 'city': user.city})
        return jsonify({'message': 'User not found'}), 404
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500
    

@rotas_controller.route('/get_users_by_city/<city>', methods=['GET'])
def get_users_by_city(city):
    pass


@rotas_controller.route('/get_users_by_service/<service>', methods=['GET'])
def get_users_by_service(service):
    pass

##vai adicionar um serviço a um usuario ( usuario vai prestar um novo serviço )
##user_id
##service_id
@rotas_controller.route('/user_service_cadaster', methods=['POST'])
def add_user_service():
    try:
        data = request.get_json()
        data = domainService.add_user_service(data['user_id'], data['service_id'])
        return jsonify({'message': 'Service added successfully',
                        "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500
