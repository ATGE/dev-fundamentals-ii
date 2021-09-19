import pytest
from truck_delivery_atge.db_connector import DBConnector
from truck_delivery_atge.client import Client
from truck_delivery_atge.client_manager import ClientManager
import json



@pytest.fixture
def db_connector(mocker) -> DBConnector:
    _ ,client =get_client_mock()
    db_conn = mocker.Mock(spec=DBConnector)
    db_conn.save.return_value = True
    db_conn.get_by_id.return_value = client
    db_conn.get_all.return_value = [client]
    db_conn.get_by_pattern.return_value =  [client]
    db_conn.delete_by_id.return_value = True
    return db_conn

def get_client_mock():
    ci_test ='123456ci'
    client =Client(
        ci = ci_test, 
        name ='testerson',
        email = 'test@mail.com',
        cellphone = '+591',
        address = 'test',
        nit = '8888',
        contract_number = '12345678')
    return ci_test, client


def test_save_document(db_connector):
    ci_test ,client = get_client_mock()
    client_manager = ClientManager(db_connector)
    result_save = client_manager.save_document(ci_test, client)
    assert result_save is True

def test_get_document(db_connector):
    ci_test ,client = get_client_mock()
    client_manager = ClientManager(db_connector)
    client_manager.save_document(ci_test, client)
    client_saved =client_manager.get_document(ci_test)
    assert client.to_dict() == client_saved.to_dict()

def test_get_all(db_connector):
    ci_test ,client = get_client_mock()
    client_manager = ClientManager(db_connector)
    client_manager.save_document(ci_test, client)
    all_saved =client_manager.get_all()
    assert all_saved[0].to_dict() == client.to_dict()


def test_delete(db_connector):
    ci_test ,client = get_client_mock()
    client_manager = ClientManager(db_connector)
    client_manager.save_document(ci_test, client)
    result =client_manager.delete(ci_test)
    assert result == True