
from truck_delivery_atge.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, _type, name, model, brand_manufacturer, driver=None):
        super(Truck, self).__init__(_type, name)
        self.model = model
        self.brand_manufacturer = brand_manufacturer
        self.driver = driver

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init

    def get_driver(self):
        return self.driver

