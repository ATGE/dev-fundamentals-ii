
from truck_delivery_atge.content_manager import ContentManager
from truck_delivery_atge.db_connector import DBConnector
from truck_delivery_atge.client import Client
from truck_delivery_atge.util import constants


CLIENTE_ID = f'{constants.UUID}-{constants.CLIENT}'

class ClientManager(ContentManager):
    def __init__(self,db_connector:DBConnector):
        self.db_connector = db_connector

    def save_document(self, ci, client:Client):
        save_result = self.db_connector.save(f'{CLIENTE_ID}-{ci}', client.to_dict())
        return save_result

    def get_document(self,ci):
        get_result = self.db_connector.get_by_id(f'{CLIENTE_ID}-{ci}')
        return get_result


    def get_all(self):
        get_result = self.db_connector.get_all(f'{CLIENTE_ID}')
        return get_result

    def delete(self, ci):
        return self.db_connector.delete_by_id(f'{CLIENTE_ID}-{ci}')