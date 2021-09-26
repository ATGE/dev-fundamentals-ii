from truck_delivery_atge.person import Person


class Driver(Person):
    """ Class representing a Driver """
    def __init__(self,ci, name, email='', cellphone='', address = '', license_number= '', license_country= ''):
        super(Driver, self).__init__(ci, name, email, cellphone, address)
        self.license_number = license_number
        self.license_country = license_country

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init

    def set_from_dict(self,dict_init):
        dict_init = self.__dict__
        return dict_init

    def entity_from_dict(data_dict):
        valid_properties ={
        'ci': '',
        'name' :'',
        'email' : '',
        'cellphone': '',
        'address' : '',
        'license_number' : '',
        'license_country' : '',
        }

        for cls_property in valid_properties.keys():
            if cls_property in data_dict:
                valid_properties[cls_property] = data_dict[cls_property]
        try:
            entity = Driver(**valid_properties)
        except Exception as e:
            raise Exception('Could not create Client \n' + repr(e))
        return entity
    


