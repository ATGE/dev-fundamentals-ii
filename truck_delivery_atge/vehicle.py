from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    """Class to define basic information of a vehicle"""

    def __init__(self, _type, name):
        self.type = _type
        self.name = name

    @abstractmethod
    def to_dict(self):
        """
        something --> This method need to be implemented
        Arg:
        """
        pass
