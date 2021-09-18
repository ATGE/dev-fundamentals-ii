from abc import ABCMeta, abstractmethod
class DBConnector(metaclass=ABCMeta):

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    @abstractmethod
    def instance(cls):
        pass

    @abstractmethod
    def save(self, id_save, object_to_save):
        pass
    
    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_pattern(self, pattern):
        pass

    @abstractmethod
    def delete_by_id(self, id):
        pass

