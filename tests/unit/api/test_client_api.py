import json
import pytest

from truck_delivery_atge.api.main import app
from truck_delivery_atge.client import Client
from truck_delivery_atge.shared_core.const import API_NAME


def get_client_mock():
    ci_test = '123456'
    name = 'testerson'
    client = Client(
        ci_test,
        name,
        email='test@mail.com',
        cellphone='+591',
        address='test',
        nit='54321',
        contract_number='987654'
    )
    return ci_test, client


@pytest.fixture
def app_client(fixture_client_manager, fixture_db_connector):
    with app.test_client() as client:
        client.application.test_client()
        yield client


@pytest.fixture
def fixture_db_connector(mocker):
    manager_route = 'truck_delivery_atge.db_connector_redis.DBConnectorRedis.'
    mocker.patch(manager_route + 'instance').return_value = mocker.Mock()


@pytest.fixture
def fixture_client_manager(mocker):
    _, client_mock = get_client_mock()
    manager_route = 'truck_delivery_atge.client_manager.ClientManager.'
    mocker.patch(manager_route + 'save_document').return_value = True
    mocker.patch(manager_route + 'get_document').return_value = client_mock
    mocker.patch(manager_route + 'get_all').return_value = [client_mock]
    mocker.patch(manager_route + 'delete').return_value = True


def test_get_client(app_client):
    _, client_expected = get_client_mock()
    client_id = 123456
    rv = app_client.get(f"{API_NAME}/client/{client_id}")
    current_client = json.loads(rv.data)

    assert client_expected.to_dict() == current_client
    assert 200 == rv.status_code


def test_get_all_clients(app_client):
    _, client_expected = get_client_mock()
    rv = app_client.get(f"{API_NAME}/client")
    current_client = json.loads(rv.data)

    assert client_expected.to_dict() == current_client[0]
    assert 200 == rv.status_code


def test_save_client(app_client):
    _, client_mock = get_client_mock()
    rv = app_client.post(f"{API_NAME}/client", json=app_client.to_dict())
    assert 200 == rv.status_code


def test_delete_client(app_client):
    client_id, _ = get_client_mock()
    rv = app_client.get(f"{API_NAME}/client/{client_id}")
    assert 200 == rv.status_code
