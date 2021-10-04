import redis
import json
import threading

from truck_delivery_atge.shared_core import configuration
from truck_delivery_atge.db_connector import DBConnector


def _get_redis():
    try:
        host = configuration.config_from_var('host')
        port = int(configuration.config_from_var('port'))
        return redis.Redis(host=host,
                           port=port)
    except (TimeoutError, ConnectionError) as timeout_e:
        raise Exception("The DB is not available",
                        custom_param="string")


class DBConnectorRedis(DBConnector):
    _instance = None
    _lock = threading.Lock()

    _instance = None

    def __init__(self):
        super(DBConnectorRedis, self).__init__()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.connection = _get_redis()
        return cls._instance

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        # close database connection
        pass

    def save(self, id_save, object_to_save):
        encode_data = json.dumps(object_to_save)
        result_save = self.connection.set(id_save, encode_data)
        return result_save

    def get_by_id(self, _id):
        result_get = self.connection.get(_id)
        decode_data = json.loads(result_get)
        return decode_data

    def get_all(self):
        list_objects = []
        list_ids = [id for id in self.connection.scan_iter(count=20)]
        if len(list_ids) > 0:
            list_objects = self.connection.mget(list_ids)
            list_objects = [json.loads(obj) for obj in list_objects]
        return list_objects

    def get_by_pattern(self, pattern):
        pattern = f"{pattern}*"
        list_objects = []
        list_ids = [id for id
                    in self.connection.scan_iter(match=pattern,
                                                 count=20)
                    ]
        if len(list_ids) > 0:
            list_objects = self.connection.mget(list_ids)
            list_objects = [json.loads(obj) for obj in list_objects]
        return list_objects

    def delete_by_id(self, _id):
        return self.connection.delete(_id)
