class Shipping:
    def __init__(self, vehicle, driver, client, start_place, end_place, packages):
        self.vehicle = vehicle
        self.driver = driver
        self.client = client
        self.start_place = start_place
        self.end_place = end_place
        self.packages = packages
        self.status = None
    
    def get_vehicle(self):
        """
        get_vehicle --> getting the vehicle
        Return:
             result(vehicle)
        """
        return self.vehicle

    def get_current_location(self):
        """
        get_current_location --> getting the current location
        Return:
             result(dict)
        """
        return self.truck.get_location()
    
    def get_current_location(self):
        """
        get_current_status --> getting the current status
        Return:
             result(status)
        """
        return self.status
