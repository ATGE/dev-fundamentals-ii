import pytest
from truck_delivery_atge.db_connector import DBConnector


@pytest.fixture
def db_connector():
    dbcon = DBConnector()

    return dbcon


def test_save_document(db_connector):
    pass


def test_get_document():
    pass


def test_get_all():
    pass


def test_delete():
    pass