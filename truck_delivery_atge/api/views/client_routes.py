"""Client routes Blueprint"""
import json

from flask import (
    Blueprint,
    jsonify,
    request,
    abort,
)

from truck_delivery_atge.shared_core.const import API_NAME as API_NAME
from truck_delivery_atge.client_manager import ClientManager
from truck_delivery_atge.client import Client
from truck_delivery_atge.db_connector_redis import DBConnectorRedis

client_app = Blueprint('client_routes', __name__)
db_connector = DBConnectorRedis.instance()
client_manager = ClientManager(DBConnectorRedis)


@client_app.route(f"{API_NAME}/client", methods=["GET"])
def list_clients():
    """
    list_clients --> list all the clients
    Args:
    Return:
        clients(dict): a list of clients
    """
    clients = [client.to_dict() for client in client_manager.get_all()]
    return jsonify(clients)


@client_app.route(f"{API_NAME}/client/<client_id>", methods=["GET"])
def get_client_by_id(client_id):
    """
    get_client_by_id --> get client by identifier
    Args:
        client_id(int): a client identifier
    Return:
        client(dict): a client
    """
    client = client_manager.get_document(client_id)
    if not client:
        abort(404, {"message": "The object not found"})
    return jsonify(client.to_dict())


@client_app.route(f"{API_NAME}/client", methods=["POST"])
def save_client():
    """
    save_client --> save a client
    Args:
    Return:
    """
    client_dict = request.json
    client = Client.entity_from_dict(client_dict)
    save_result = client_manager.save_document(client)
    if not save_result:
        abort(422)
    return jsonify({"message": "The object was saved successfully"})


@client_app.route(f"{API_NAME}/client/<client_id>", methods=["DELETE"])
def delete_client(client_id):
    """
    delete_client --> delete a client
    Args:
         client_id(int): a client identifier
    Return:
    """
    delete_result = client_manager.delete(client_id)
    if not delete_result:
        abort(404, {"message": "The object not found"})
    return jsonify({"message": "The object was deleted successfully"})
