
from truck_delivery_atge.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self,type, name,model ,brand_manufactor,driver=None):
        super(Truck, self).__init__(type, name)
        self.model = model
        self.brand_manufactor = brand_manufactor
        self.driver = driver

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init

    def get_driver(self):
        return self.driver

