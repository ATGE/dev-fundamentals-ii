from truck_delivery_atge.db_connector import DBConnector
import redis
import json
import threading


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
            cls.connection = redis.Redis(host="localhost",
                                         port=6379)
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

    def get_by_id(self, id):
        result_get = self.connection.get(id)
        decode_data = json.loads(result_get)
        return decode_data

    def get_all(self):
        list_objs = []
        list_ids = [id for id in self.connection.scan_iter(count=20)]
        if len(list_ids) > 0:
            list_objs = self.connection.mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
        return list_objs

    def get_by_pattern(self, pattern):
        pattern = f"{pattern}*"
        list_objs = []
        list_ids = [id for id
                    in self.connection.scan_iter(match=pattern,
                                                 count=20)
                    ]
        if len(list_ids) > 0:
            list_objs = self.connection.mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
        return list_objs

    def delete_by_id(self, id):
        return self.connection.delete(id)
