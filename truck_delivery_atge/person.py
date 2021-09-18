from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """Class to define basic information of a person"""

    def __init__(self, ci, name, email, cellphone):
        self.name = name
        self.ci = ci
        self.email = email
        self.cellphone = cellphone

    @abstractmethod
    def to_dict(self):
        """
        something --> This method need to be implemented
        Arg:
        """
        pass

