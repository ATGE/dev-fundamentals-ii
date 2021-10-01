from truck_delivery_atge.content_manager import ContentManager
from truck_delivery_atge.db_connector import DBConnector
from truck_delivery_atge.client import Client
from truck_delivery_atge.shared_core import constants
from truck_delivery_atge.db_connector_redis import DBConnectorRedis
from truck_delivery_atge.shared_core.exceptions import CustomException, DataNotAvailableException

CLIENT_ID = f'{constants.UUID}-{constants.CLIENT}'


class ClientManager(ContentManager):
    def __init__(self, db_connector: DBConnector = None):
        self.db_connector = db_connector if db_connector else DBConnectorRedis.instance()

    def save_document(self, ci, client: Client) -> bool:
        try:
            _id = f'{CLIENT_ID}-{ci}'
            client_json = client.to_dict()
            return self.db_connector.save(_id, client_json)
        except CustomException as c:
            raise DataNotAvailableException('Could not create Client \n' + repr(c))

    def get_document(self, ci) -> Client:
        try:
            _id = f'{CLIENT_ID}-{ci}'
            get_result = self.db_connector.get_by_id(_id)
            return get_result

        except CustomException as c:
            raise DataNotAvailableException('Could not get Client \n' + repr(c))

    def get_all(self) -> list:
        try:
            get_result = self.db_connector.get_all()
            return get_result

        except CustomException as c:
            raise DataNotAvailableException('Could not get Clients \n' + repr(c))

    def delete(self, ci) -> bool:
        try:
            _id = f'{CLIENT_ID}-{ci}'
            get_result = self.db_connector.delete_by_id(_id)
            return get_result

        except CustomException as c:
            raise DataNotAvailableException('Could not delete Clients \n' + repr(c))
