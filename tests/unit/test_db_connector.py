import pytest
import json
from truck_delivery_atge.db_connector_redis import DBConnectorRedis


@pytest.fixture
def fixture_db_connector(mocker):
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)
    mocker.patch("redis.Redis.scan_iter").return_value = "123"
    mocker.patch("redis.Redis.mget").return_value = [json.dumps(object_to_save)]
    mocker.patch("redis.Redis.delete").return_value = 1
    db_conn = DBConnectorRedis.instance()
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
    with DBConnectorRedis.instance() as db_connector:
        db_connector.save(id_test, object_to_save)
        result = db_connector.get_by_id(id_test)
    assert result

def test_get_all_mock(fixture_db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    fixture_db_connector.save(id_test, object_to_save)
    result = fixture_db_connector.get_all()
    assert isinstance(result, list) == True
    assert result[0] == object_to_save

def delete_by_id_mock(fixture_db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    fixture_db_connector.save(id_test,object_to_save)
    result = fixture_db_connector.delete(id_test)
    assert result == 1
