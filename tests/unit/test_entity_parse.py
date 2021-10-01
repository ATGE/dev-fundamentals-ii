import pytest

from truck_delivery_atge.driver import Driver
from truck_delivery_atge.client import Client


def test_client_entity_from_dict():
    client_dict = {
        'ci': '123456',
        'name': 'testerson',
        'email': 'test@mail.com',
        'cellphone': '+591',
        'address': 'test',
        'nit': '8888',
        'contract_number': '12345678',
    }
    client = Client.entity_from_dict(client_dict)
    client_dict.pop('nit')
    assert client.to_dict() == client_dict


def test_driver_entity_from_dict():
    driver_dict = {
        'ci': '123456',
        'name': 'testerson',
        'email': 'test@mail.com',
        'cellphone': '+591',
        'address': 'test',
        'license_number': '8888',
        'license_country': '12345678',
    }
    client = Driver.entity_from_dict(driver_dict)
    assert client.to_dict() == driver_dict
