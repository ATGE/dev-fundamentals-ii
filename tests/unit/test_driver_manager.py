import pytest
from truck_delivery_atge.db_connector import DBConnector
from truck_delivery_atge.driver import Driver
from truck_delivery_atge.driver_manager import DriverManager


@pytest.fixture
def db_connector(mocker) -> DBConnector:
    _, driver = get_driver_mock()
    db_conn = mocker.Mock(spec=DBConnector)
    db_conn.save.return_value = True
    db_conn.get_by_id.return_value = driver
    db_conn.get_all.return_value = [driver]
    db_conn.get_by_pattern.return_value = [driver]
    db_conn.delete_by_id.return_value = True
    return db_conn


def get_driver_mock():
    ci_test = '123456ci'
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


def test_save_document(db_connector):
    ci_test, client = get_driver_mock()
    driver_manager = DriverManager(db_connector)
    result_save = driver_manager.save_document(ci_test, client)
    assert result_save is True


def test_get_document(db_connector):
    ci_test, client = get_driver_mock()
    driver_manager = DriverManager(db_connector)
    driver_manager.save_document(ci_test, client)
    client_saved = driver_manager.get_document(ci_test)
    assert client.to_dict() == client_saved.to_dict()


def test_get_all(db_connector):
    ci_test, client = get_driver_mock()
    driver_manager = DriverManager(db_connector)
    driver_manager.save_document(ci_test, client)
    all_saved = driver_manager.get_all()
    assert all_saved[0].to_dict() == client.to_dict()


def test_delete(db_connector):
    ci_test, client = get_driver_mock()
    driver_manager = DriverManager(db_connector)
    driver_manager.save_document(ci_test, client)
    result = driver_manager.delete(ci_test)
    assert result == True
