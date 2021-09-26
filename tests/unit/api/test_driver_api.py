import json
import pytest

from truck_delivery_atge.api.main import app
from truck_delivery_atge.driver import Driver
from truck_delivery_atge.shared_core.const import API_NAME


def get_driver_mock():
    ci_test = '123456'
    name = 'testerson'
    driver = Driver(
        ci_test,
        name,
        email='test@mail.com',
        cellphone='+591',
        address='test',
        license_number='8888',
        license_country='MOON')
    return ci_test, driver


@pytest.fixture
def client(fixture_driver_manager, fixture_db_connector):
    with app.test_client() as client:
        client.application.test_client()
        yield client


@pytest.fixture
def fixture_db_connector(mocker):
    manager_route = 'truck_delivery_atge.db_connector_redis.DBConnectorRedis.'
    mocker.patch(manager_route + 'instance').return_value = mocker.Mock()


@pytest.fixture
def fixture_driver_manager(mocker):
    _, driver = get_driver_mock()
    manager_route = 'truck_delivery_atge.driver_manager.DriverManager.'
    mocker.patch(manager_route + 'save_document').return_value = True
    mocker.patch(manager_route + 'get_document').return_value = driver
    mocker.patch(manager_route + 'get_all').return_value = [driver]
    mocker.patch(manager_route + 'delete').return_value = True


def test_main_index(client):
    rv = client.get('/')

    message = bytes(f"Transportation company API: {API_NAME}", 'utf-8')

    assert message == rv.data
    assert 200 == rv.status_code


def test_get_driver(client):
    _, driver_expected = get_driver_mock()
    driver_id = 123456
    rv = client.get(f"{API_NAME}/driver/{driver_id}")
    current_driver = json.loads(rv.data)

    assert driver_expected.to_dict() == current_driver
    assert 200 == rv.status_code


def test_get_all_driver(client):
    _, driver_expected = get_driver_mock()
    rv = client.get(f"{API_NAME}/driver")
    current_driver = json.loads(rv.data)

    assert driver_expected.to_dict() == current_driver[0]
    assert 200 == rv.status_code


def test_save_driver(client):
    _, driver = get_driver_mock()
    rv = client.post(f"{API_NAME}/driver", json=driver.to_dict())
    assert 200 == rv.status_code


def test_delete_driver(client):
    driver_id, _ = get_driver_mock()
    rv = client.get(f"{API_NAME}/driver/{driver_id}")
    assert 200 == rv.status_code
