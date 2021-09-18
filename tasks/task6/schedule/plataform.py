from sender import Sender
class MessagePlataform:
    """
    Class to receive a message from a Sender and is able to notify it.
    """

    def set_sender(self, sender:Sender):
        self.__sender = sender

    def notify_sender(self):
        self.__sender.update()

    def send_message(self, msg):
        pass
    def receive_message(self, msg):
        pass

