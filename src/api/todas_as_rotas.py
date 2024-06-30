from flask import Flask, jsonify, request, Blueprint
from adapters.sqlalchemyrepositories import SqlAchemyRepositories
from domain.services.service import Service
from domain.services.user_service import UserService
from infraestructure.db_setup import db
from infraestructure.dbscript import PopulateDB

repositories = SqlAchemyRepositories(db=db)
domainService = Service(repositories)
domainUserService = UserService(repositories)

populateDB = PopulateDB(db=db)

rotas_controller = Blueprint('api', __name__)
#http://127.0.0.1/api/teste
@rotas_controller.route("/teste", methods=['GET'])
def teste():
    return jsonify({'message': 'Teste'})

@rotas_controller.route('/populate_db', methods=['GET'])
def populate_db():
    try:
        db.create_all()
    except:
        print("Tables already created")
    try:
        populateDB.populate()
        return jsonify({'message': 'Database populated successfully',})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500

@rotas_controller.route('/drop_db', methods=['GET'])
def drop_db():
    try:
        populateDB.drop_all_with_cascade()
        return jsonify({'message': 'Database dropped successfully',})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500
    
@rotas_controller.route('/create_user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        data = domainUserService.create_user(data['name'], data['email'], data['state'], data['city'], data['user_type'])
        return jsonify({'message': 'User created successfully!',
                        "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500
    
#http://127.0.0.1:5000/api/get_user_by_email/teste@asd.comdomainService = Service(repositories)
@rotas_controller.route('/get_user_by_email/<email>', methods=['GET'])
def get_user_by_email(email):
    try:
        user = domainUserService.get_user_by_email(email)
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
    try:
        users = domainUserService.get_users_by_city(city)
        return jsonify(users), 200
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500
    

@rotas_controller.route('/get_users_by_state/<state>', methods=['GET'])
def get_users_by_state(state):
    try:
        users = domainUserService.get_users_by_state(state)
        return jsonify(users), 200
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500




@rotas_controller.route('/get_users_by_service/<service>', methods=['GET'])
def get_users_by_service(service):
    try:
        users = domainUserService.get_users_by_service(service)
        return jsonify(users), 200
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal server error'}), 500

##vai adicionar um serviço a um usuario ( usuario vai prestar um novo serviço )
##user_id
##service_id
@rotas_controller.route('/user_service_cadaster', methods=['POST'])
def add_user_service():
    try:
        data = request.get_json()
        data = domainUserService.add_user_service(data['user_id'], data['service_id'])
        return jsonify({'message': 'Service added successfully',
                        "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

## requisição de trabalho entre o contratante e o contratado selecionado
## solicitar serviço id cliente e prestador e tipo de serviço
### ATE ESSA ROTA AQUI FOI TESTADA E ESTA FUNCIONANDO
@rotas_controller.route('/request_service_order', methods=['POST'])
def request_service():
    try:
        data = request.get_json()
        data = domainService.request_service_order(data['client_id'], data['provider_id'], data['service_type'])
        return jsonify({'message': 'Service requested successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500


## solicitação para envio do orcamento id serviceOrder e valor do orcamento
@rotas_controller.route('/send_service_order_value', methods=['POST'])
def send_quote():
    try:
        data = request.get_json()
        data = domainService.send_service_order_value(data['service_order_id'], data['quote_value'])
        return jsonify({'message': 'Quote sent successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

## aceitar ou rejeitar orcamento id service order  -> aceitar e rejeijar
@rotas_controller.route('/accept_quote', methods=['POST'])
def accept_quote():
    try:
        data = request.get_json()
        data = domainService.accept_quote(data['service_order_id'])
        return jsonify({'message': 'Quote accepted successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

@rotas_controller.route('/reject_quote', methods=['POST'])
def reject_quote():
    try:
        data = request.get_json()
        data = domainService.reject_quote(data['service_order_id'])
        return jsonify({'message': 'Quote rejected successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

## reabrir a ordem de serviço 
@rotas_controller.route('/reopen_service_order', methods=['POST'])
def reopen_service_order():
    try:
        data = request.get_json()
        data = domainService.reopen_service_order(data['service_order_id'])
        return jsonify({'message': 'Service order reopened successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

## finalizar por parte do prestador
@rotas_controller.route('/provider_finalize_service', methods=['POST'])
def provider_finalize_service():
    try:
        data = request.get_json()
        data = domainService.provider_finalize_service(data['service_order_id'])
        return jsonify({'message': 'Service finalized by provider successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

## roda finalizar por parte do cliente
@rotas_controller.route('/client_finalize_service', methods=['POST'])
def client_finalize_service():
    try:
        data = request.get_json()
        data = domainService.client_finalize_service(data['service_order_id'])
        return jsonify({'message': 'Service finalized by client successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

## rota para finalizar de vez o serviço
@rotas_controller.route('/finalize_service', methods=['POST'])
def finalize_service():
    try:
        data = request.get_json()
        data = domainService.finalize_service(data['service_order_id'])
        return jsonify({'message': 'Service finalized successfully', "data": data})
    except ValueError as e:
        print(e)
        return jsonify({'message': f'{str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500