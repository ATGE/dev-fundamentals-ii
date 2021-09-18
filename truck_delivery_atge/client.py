from truck_delivery_pamy.person import Person


class Client(Person):
    """ Class representing a Client """
    def __init__(self, name, email, cellphone, address, nit):
        super(Client, self).__init__(name, email, cellphone, address)
        self.nit = nit

    def to_dict(self):
        dict_init = self.__dict__
        dict_init.pop("nit", None)
        return dict_init


