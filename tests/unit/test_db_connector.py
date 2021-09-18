import pytest
import json
from truck_delivery_pamy.db_connector import DBConnector


@pytest.fixture
def fixture_db_connector(mocker):
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)
    db_conn = DBConnector()
    return db_conn


def test_save_mock(fixture_db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    result_save = fixture_db_connector.save(id_test, object_to_save)
    assert result_save is True


def test_get_by_id_mock(fixture_db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    fixture_db_connector.save(id_test, object_to_save)
    result = fixture_db_connector.get_by_id(id_test)
    assert result == object_to_save


def test_get_by_id_mock_as_context_manager(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)

    result = None
    with DBConnector() as db_connector:
        db_connector.save(id_test, object_to_save)
        result = db_connector.get_by_id(id_test)
    assert result
