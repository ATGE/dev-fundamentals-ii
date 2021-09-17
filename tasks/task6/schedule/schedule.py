import time
from sender import Sender
from plataform import MessagePlataform

class Schedule(Sender):
    def __init__(self,hour=0,minute=0,second=0):
        super().__init__()
        self.hours = hour
        self.minutes = minute
        self.seconds = second
        self.period = 0
        self.plataforms = []
        self.message = 'test message'
        self.message_received = False
        self.time_to_wait_in_seconds = 1

    def set_time(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second
        self.period = 0
        
    def set_time_by_period(self,period):
        self.period = period
        self.start_time = False
    
    def add_plataforms(self,plataform : MessagePlataform):
        plataform.set_sender(self)
        self.plataforms.append(plataform)
    
    def set_message(self,message):
        self.message = message

    def run(self):
        while self.period:
            for plataform in self.plataforms:
                plataform.receive_message(self.message)
                time.sleep(self.time_to_wait_in_seconds)
                if self.message_received:
                    return
        self._sleep()           
        for plataform in self.plataforms:
                plataform.receive_message(self.message)
                time.sleep(self.time_to_wait_in_seconds)
                if self.message_received:                    
                    return

    def _get_time_in_seconds(self):
        return self.hours*60 + self.minutes*60 + self.seconds

    def _get_period_in_seconds(self):
        return self.period * 3600

    def _sleep(self):
        time.sleep(self._get_time_in_seconds())
    
    def update(self):
        self.message_received = True
        print('message successfully received')




