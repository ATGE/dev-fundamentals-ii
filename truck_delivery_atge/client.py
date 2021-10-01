from truck_delivery_atge.person import Person


class Client(Person):
    """ Class representing a Client """

    def __init__(self, ci, name, email='', cellphone='', address='', nit='', contract_number=''):
        super(Client, self).__init__(ci, name, email, cellphone, address)
        self.nit = nit
        self.contract_number = contract_number

    def to_dict(self):
        dict_init = self.__dict__
        dict_init.pop("nit", None)
        return dict_init

    def entity_from_dict(data_dict):
        valid_properties = {
            'ci': '',
            'name': '',
            'email': '',
            'cellphone': '',
            'address': '',
            'nit': '',
            'contract_number': '',
        }

        for cls_property in valid_properties.keys():
            if cls_property in data_dict:
                valid_properties[cls_property] = data_dict[cls_property]
        try:
            entity = Client(**valid_properties)
        except Exception as e:
            raise Exception('Could not create Client \n' + repr(e))
        return entity
