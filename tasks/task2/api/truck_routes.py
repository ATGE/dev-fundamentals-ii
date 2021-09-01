"""Trucks routes Blueprint"""

from const import API_NAME as API_NAME
from flask import (
    Blueprint,
    jsonify,
    request
)

from truck import trucks as trucks
from driver import drivers as drivers
import utils

truck_app = Blueprint('truck_routes', __name__)


@truck_app.route(f"{API_NAME}/trucks", methods=["GET"])
def list_trucks():
    """
    list_trucks --> list all the trucks
    Args:
    Return:
        trucks(dict): a list of trucks
    """
    return jsonify(trucks)


@truck_app.route(f"{API_NAME}/trucks/<truck_id>", methods=["GET"])
def get_truck_by_id(truck_id):
    """
    get_truck_by_id --> get truck by identifier
    Args:
        truck_id(int): a truck identifier
    Return:
        trucks(dict): a truck
    """
    return jsonify(utils.get_dict_by_key_value_from_list('id', truck_id, trucks))


@truck_app.route(f"{API_NAME}/trucks", methods=["POST"])
def save_truck():
    """
    save_truck --> save a truck
    Args:
    Return:
    """
    truck_json = request.json
    trucks.append(truck_json)
    return jsonify({"message": "The object was saved successfully"})

@truck_app.route(f"{API_NAME}/trucks/<truck_id>", methods=["DELETE"])
def delete_truck(truck_id):
    """
    delete_truck --> delete a truck
    Args:
         truck_id(int): a truck identifier
    Return:
    """
    truck = utils.get_dict_by_key_value_from_list('id', truck_id, trucks)
    if truck:
        trucks.remove(truck)
        return jsonify({"message": "The object was deteled successfully"})
    return jsonify({"message": "Object not found"})
