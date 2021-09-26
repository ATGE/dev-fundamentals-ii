
from truck_delivery_atge.content_manager import ContentManager
from truck_delivery_atge.db_connector import DBConnector
from truck_delivery_atge.driver import Driver

from truck_delivery_atge.util import constants


DRIVER_ID = f'{constants.UUID}-{constants.DRIVER}'

class DriverManager(ContentManager):
    def __init__(self,db_connector:DBConnector):
        self.db_connector = db_connector

    def save_document(self, ci, driver:Driver):
        save_result = self.db_connector.save(f'{DRIVER_ID}-{ci}', driver.to_dict())
        return save_result

    def get_document(self,ci):
        get_result = self.db_connector.get_by_id(f'{DRIVER_ID}-{ci}')
        return get_result


    def get_all(self):
        get_result = self.db_connector.get_all(f'{DRIVER_ID}')
        return get_result

    def delete(self, ci):
        return self.db_connector.delete_by_id(f'{DRIVER_ID}-{ci}')