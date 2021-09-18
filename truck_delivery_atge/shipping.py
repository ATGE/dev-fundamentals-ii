class Shipping:
    def __init__(self, truck, driver, client):
        self.truck = truck
        self.driver = driver
        self.client = client

    def get_current_location(self):
        """
        get_current_location --> getting the current location
        Return:
             result(dict)
        """
        return self.truck.get_location()
