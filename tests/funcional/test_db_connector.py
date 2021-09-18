import pytest
from truck_delivery_atge.db_connector import DBConnector

def test_save():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DBConnector.instance()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save


def test_get_by_id():
    id_test = "123"
    object_to_save = {"123": {"a":"a"}}

    db_connector = DBConnector.instance()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


