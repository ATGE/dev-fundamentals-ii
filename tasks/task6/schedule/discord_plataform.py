from plataform import MessagePlataform
import time

class DiscordPlataform(MessagePlataform):

    def __init__(self):
        super().__init__()
        
    def receive_message(self, msg):
        print('receiving discord message :', msg)
        time.sleep(1)
        self.notify_sender()

