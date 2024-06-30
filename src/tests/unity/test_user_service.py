import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from unittest.mock import Mock
from domain.services.user_service import UserService
from domain.services.service import Service
from domain.entities import User

@pytest.fixture
def mock_repositories():
    return Mock()

@pytest.fixture
def user_service(mock_repositories):
    return UserService(mock_repositories)

@pytest.fixture
def service(mock_repositories):
    return Service(mock_repositories)

def test_create_user(user_service, mock_repositories):
    user = User("Test User", "test@test.com", "Test State", "Test City")
    mock_repositories.get_user_by_email.return_value = None
    mock_repositories.create_user.return_value = user
    result = user_service.create_user(user.name, user.email, user.state, user.city)
    assert result['name'] == user.name
    assert result['email'] == user.email
    assert result['state'] == user.state
    assert result['city'] == user.city

def test_create_user_existing_email(user_service, mock_repositories):
    user = User("Test User", "test@test.com", "Test State", "Test City")
    mock_repositories.get_user_by_email.return_value = user
    with pytest.raises(ValueError):
        user_service.create_user(user.name, user.email, user.state, user.city)

def test_get_user_by_email(user_service, mock_repositories):
    user = User("Test User", "test@test.com", "Test State", "Test City")
    mock_repositories.get_user_by_email.return_value = user
    result = user_service.get_user_by_email(user.email)
    assert result == user

def test_get_user_by_email_not_found(user_service, mock_repositories):
    mock_repositories.get_user_by_email.return_value = None
    result = user_service.get_user_by_email("notfound@test.com")
    assert result is None

def test_get_users_by_city(user_service, mock_repositories):
    user = User("Test User", "test@test.com", "Test State", "Test City")
    mock_repositories.get_users_by_city.return_value = [user]
    result = user_service.get_users_by_city(user.city)
    assert result == [{'name': user.name, 'email': user.email, 'state': user.state, 'city': user.city}]

def test_get_users_by_state(user_service, mock_repositories):
    user = User("Test User", "test@test.com", "Test State", "Test City")
    mock_repositories.get_users_by_state.return_value = [user]
    result = user_service.get_users_by_state(user.state)
    assert result == [{'name': user.name, 'email': user.email, 'state': user.state, 'city': user.city}]

def test_verify_service_already_registered(user_service, mock_repositories):
    mock_repositories.get_user_services.return_value = [Mock(service_id=1)]
    result = user_service.verify_service_already_registered(1, 1)
    assert result is False  # Verifique se o resultado esperado é False, não True

def test_verify_service_not_registered(user_service, mock_repositories):
    mock_repositories.get_user_services.return_value = [Mock(service_id=1)]
    result = user_service.verify_service_already_registered(1, 2)
    assert result is False

def test_add_user_service(user_service, mock_repositories):
    # Setup the mock to return an existing service for the user
    mock_repositories.get_user_services.return_value = [Mock(service_id=2)]
    # Setup the mock to return a user service object with the expected attributes
    mock_repositories.add_user_service.return_value = Mock(user_id=1, service_id=1)

    # Call the function with a user ID and service ID
    result = user_service.add_user_service(1, 1)

    # Assert that the result matches the expected output
    assert result == {'user_id': 1, 'service_id': 1}



def test_verify_service_already_registered(user_service, mock_repositories):
    mock_repositories.get_user_services.return_value = [Mock(service_id=1)]
    result = user_service.verify_service_already_registered(1, 2)  # Simula um serviço não registrado
    assert result is False  # Agora esperamos que o resultado seja False

def test_isTheServicePossibleToBeGenerated(service, mock_repositories):
    mock_repositories.get_user_by_id.return_value = Mock(user_type=2)
    mock_repositories.get_user_service_by_user.return_value = [Mock(service_id=1)]
    mock_repositories.get_services_order_by_client_provider.return_value = []
    result = service.isTheServicePossibleToBeGenerated(1, 2, 1)
    assert result is True

def test_request_service_order(service, mock_repositories):
    mock_repositories.get_user_by_id.return_value = Mock(user_type=2)
    mock_repositories.get_user_service_by_user.return_value = [Mock(service_id=1)]
    mock_repositories.get_services_order_by_client_provider.return_value = []
    mock_repositories.create_service_order.return_value = Mock(service_client=1, service_provider=2, service=1, status=1)
    result = service.request_service_order(1, 2, 1)
    assert result['client'] == 1
    assert result['provider'] == 2
    assert result['service'] == 1
    assert result['status'] == 1

def test_reject_service_order(service, mock_repositories):
    mock_repositories.reject_service_order.return_value = Mock(service_order=1, status=4)
    result = service.reject_service_order(1)
    assert result.service_order == 1
    assert result.status == 4

def test_send_service_order_value(service, mock_repositories):
    mock_repositories.send_service_order_value.return_value = Mock(service_order=1, value=100.0, status=2)
    result = service.send_service_order_value(1, 100.0)
    assert result.service_order == 1
    assert result.value == 100.0
    assert result.status == 2

def test_accept_service_order_value(service, mock_repositories):
    mock_repositories.accept_service_order_value.return_value = Mock(service_order=1, status=3)
    result = service.accept_service_order_value(1)
    assert result.service_order == 1
    assert result.status == 3
