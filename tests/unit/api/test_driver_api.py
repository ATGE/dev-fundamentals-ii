import json
import pytest

from truck_delivery_atge.api.main import app
from truck_delivery_atge.driver_manager import DriverManager
from truck_delivery_atge.driver import Driver
from truck_delivery_atge.shared_core.const import API_NAME


def get_driver_mock():
    ci_test ='123456'
    name ='testerson'
    driver =Driver(
        ci_test, 
        name,
        email = 'test@mail.com',
        cellphone = '+591',
        address = 'test',
        license_number = '8888',
        license_country = 'MOON')
    return ci_test, driver


@pytest.fixture
def driver_manager(mocker) -> DriverManager:
    _ ,driver =get_driver_mock()
    manager = mocker.Mock()
    manager.save.return_value = True
    manager.get_by_id.return_value = driver
    manager.get_all.return_value = [driver]
    manager.get_by_pattern.return_value =  [driver]
    manager.delete_by_id.return_value = True
    return manager

@pytest.fixture
def fixture_db_connector(mocker):
    db_connector = mocker.Mock()
    db_connector.instance.return_value = mocker.Mock()
    return db_connector

@pytest.fixture
def client(driver_manager,fixture_db_connector):
    with app.test_client() as client:
        yield client


def test_main_index(client):
    rv = client.get('/')

    message =bytes(f"Transportation company API: {API_NAME}", 'utf-8')

    assert message == rv.data

def test_get_driver(client,driver_manager,fixture_db_connector):
    _, driver_expected =get_driver_mock()
    driver_id = 123456
    rv = client.get(f"{API_NAME}/driver/{driver_id}")
    current_driver =rv.data
    assert driver_expected == current_driver