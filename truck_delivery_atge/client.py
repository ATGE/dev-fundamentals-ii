from truck_delivery_atge.person import Person


class Client(Person):
    """ Class representing a Client """
    def __init__(self,ci, name, email='', cellphone='', address = '', nit='', contract_number=''):
        super(Client, self).__init__(ci, name, email, cellphone, address)
        self.nit = nit
        self.contract_number = contract_number

    def to_dict(self):
        dict_init = self.__dict__
        dict_init.pop("nit", None)
        return dict_init


