from plataform import MessagePlataform
import time

class SkypePlataform(MessagePlataform):

    def __init__(self):
        super().__init__()

    def receive_message(self, msg):
        print('receiving skype message :', msg)
        time.sleep(10)
        self.notify_sender()

