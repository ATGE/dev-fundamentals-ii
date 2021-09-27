import pytest
from truck_delivery_atge.db_connector import DBConnector
from truck_delivery_atge.client import Client
from truck_delivery_atge.client_manager import ClientManager
import json

from truck_delivery_atge.shared_core import configuration


def test_default_configuration():
    host = configuration.config_from_var('host')
    port = configuration.config_from_var('port')

    assert host == 'localhost'
    assert port == '6739'
