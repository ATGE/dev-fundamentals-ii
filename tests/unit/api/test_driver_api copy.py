import json
import pytest

from truck_delivery_atge.api.main import app
from truck_delivery_atge.driver_manager import DriverManager
from truck_delivery_atge.driver import Driver


def get_driver_mock():
    ci_test ='123456ci'
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
def driver_nameger(mocker) -> DriverManager:
    _ ,driver =get_driver_mock()
    manager = mocker.Mock()
    manager.save_document.return_value = True
    manager.get_document.return_value = driver
    manager.get_all.return_value = [driver]
    manager.delete.return_value = True
    return manager


def test_main_exception():
    with app.test_client() as client:
        rv = client.get('/')

    assert b'Index Page' == rv.data


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_main_index(client):
    rv = client.get('/')

    assert b'Index Page' == rv.data

    assert 200 == rv.status_code


def test_save_book(client, driver_nameger):
    driver_dict ={
        'ci': '123456',
        'name' :'testerson',
        'email' : 'test@mail.com',
        'cellphone': '+591',
        'address' : 'test',
        'license_number' : '8888',
        'license_country' : '12345678',
    }
    rv = client.post('/driver',

                     headers={"Content-Type": "application/json"},

                     json=json.dumps(driver_dict))

    assert rv.status_code == 200
