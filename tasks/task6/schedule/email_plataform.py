from plataform import MessagePlataform
import time

class EmailPlataform(MessagePlataform):

    def receive_message(self, msg):
        print('receiving email message :', msg)
        time.sleep(10)
        self.notify_sender()

