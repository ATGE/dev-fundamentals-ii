from plataform import MessagePlataform
import time

class SlackPlataform(MessagePlataform):

    def __init__(self):
        super().__init__()
        
    def receive_message(self, msg):
        print('receiving slack message :', msg)
        time.sleep(10)
        self.notify_sender()

