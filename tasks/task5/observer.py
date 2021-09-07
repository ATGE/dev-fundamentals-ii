# Based on https://dev.to/jemaloqiu/design-pattern-in-python-2-observer-j4

class AbstractObservable():
    """
        Abstract Observable 
    """

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, arg=0):
        for o in self.__observers:
            o.update(self, arg)


class AbstractObserver():
    """
        Abstract Observer - Abstract device
    """

    def __init__(self):
        pass

    def update(self):  
        pass

#
class MonitorTruck(AbstractObservable):
    """
        Concrete Observable class
    """

    def __init__(self, name):
        super().__init__()  
        self.name = name
        self.__physical_properties = {"temperature": 0.0, "humidity": 0.0}

    def set_value(self, measure_key, val):
        if measure_key in self.__physical_properties:
            self.__physical_properties[measure_key] = val
            self.notify_observers()
        else:
            print(f"Parameter type {measure_key} not supported.")

    def get_value(self, measure_key):
        return self.__physical_properties.get(measure_key)

class Thermometer(AbstractObserver):      
    """
        Concrete Observer - Thermometer
    """

    def __init__(self):
        super().__init__()


    def update(self, tt, obj):
        if tt.__class__ == MonitorTruck:
            temperature = tt.get_value("temperature")
            if temperature > 37.8:
                print(f"WARNING - Temperature too high: {temperature}" )
            elif temperature < 36.0:
                print(f"WARNING - Temperature too slow: {temperature}")
            else:
                print(f"INFO - Temperature normal: {temperature}")

        else:
            pass

class HumidityMeter(AbstractObserver):      
    """
        Concrete Observer - humidity meter
    """

    def __init__(self):
        super().__init__()

    def update(self, tt, obj):
        if tt.__class__ == MonitorTruck:
            humidity_value = tt.get_value("humidity")
            if humidity_value > 60:
                print(f"WARNING - humidity too high: {humidity_value}" )
            elif humidity_value < 40:
                print(f"WARNING - humidity too high: {humidity_value}" )
            else:
                print(f"INFO - humidity normal: {humidity_value}")

        else:
            pass

import time

if __name__ == "__main__":
    tuck = MonitorTruck("John")
    thermometer = Thermometer()
    humidity = HumidityMeter()


    ## now kick off the simulation 
    for i in range(0, 15):

        time.sleep(1.5)
        print("====== Time step {} =======".format(i+1))

        # At rount #3: thermometer is added for monitoring temperature
        # At rount #5: humidity is added for monitoring the humidity level
        # At rount #10: thermometer is removed

        if i == 3:
            tuck.add_observer(thermometer)        
        elif i == 5:        
            tuck.add_observer(humidity)        
        elif i == 10:
            tuck.remove_observer(thermometer)

        # simulating the  physical parameters
        if i%3 ==0:
            tuck.set_value("temperature", 35.5 + 0.5*i)
        elif i%3 == 1:
            tuck.set_value("humidity", 30 + 3*i)
    