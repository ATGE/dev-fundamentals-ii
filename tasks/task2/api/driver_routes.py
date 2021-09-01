"""Driver routes Blueprint"""

from const import API_NAME as API_NAME
from flask import (
    Blueprint,
    jsonify,
    request
)

from truck import trucks as trucks
from driver import drivers as drivers
import utils

driver_app = Blueprint('driver_routes', __name__)


@driver_app.route(f"{API_NAME}/driver", methods=["GET"])
def list_drivers():
    """
    list_drivers --> list all the drivers
    Args:
    Return:
        drivers(dict): a list of drivers
    """
    return jsonify(drivers)


@driver_app.route(f"{API_NAME}/driver/<driver_id>", methods=["GET"])
def get_driver_by_id(driver_id):
    """
    get_driver_by_id --> get driver by identifier
    Args:
        driver_id(int): a driver identifier
    Return:
        driver(dict): a driver
    """
    return jsonify(utils.get_dict_by_key_value_from_list('id', driver_id, drivers))


@driver_app.route(f"{API_NAME}/driver/<identifier>/truck", methods=["GET"])
def get_truck_by_driver_id(identifier):
    """
    get_truck_by_driver_id --> get truck by driver identifier, it can be id or name
    Args:
        identifier(string): a driver identifier
    Return:
        truck(dict): a truck
    """
    key = 'name'
    if identifier.isdigit():
        key = 'id'

    truck_to_return = {}
    driver = utils.get_dict_by_key_value_from_list(
        key, identifier, drivers)
    truck_to_return = utils.get_dict_by_key_value_from_list(
        'id', driver.get('id'), trucks)
    return jsonify(truck_to_return)


@driver_app.route(f"{API_NAME}/driver", methods=["POST"])
def save_driver():
    """
    save_driver --> save a driver
    Args:
    Return:
    """
    driver_json = request.json
    drivers.append(driver_json)

    return jsonify({"message": "The object was saved successfully"})


@driver_app.route(f"{API_NAME}/driver/<driver_id>", methods=["DELETE"])
def delete_driver(driver_id):
    """
    delete_driver --> delete a driver
    Args:
         driver_id(int): a driver identifier
    Return:
    """
    driver = utils.get_dict_by_key_value_from_list('id', driver_id, drivers)
    if driver:
        drivers.remove(driver)
        return jsonify({"message": "The object was deteled successfully"})
    return jsonify({"message": "Object not found"})
