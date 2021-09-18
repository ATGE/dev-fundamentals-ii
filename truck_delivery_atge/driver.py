from truck_delivery_atge.person import Person


class Driver(Person):
    """ Class representing a Driver """
    def __init__(self, name, email, cellphone, address, license_number, license_country):
        super(Driver, self).__init__(name, email, cellphone, address)
        self.license_number = license_number
        self.license_country = license_country

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init


