"""Driver routes Blueprint"""
import json

from flask import (
    Blueprint,
    jsonify,
    request
)

from truck_delivery_atge.shared_core.const import API_NAME as API_NAME
from truck_delivery_atge.driver_manager import DriverManager
from truck_delivery_atge.driver import Driver
from truck_delivery_atge.db_connector_redis import DBConnectorRedis

driver_app = Blueprint('driver_routes', __name__)
db_connector = DBConnectorRedis.instance()
driver_manager = DriverManager(DBConnectorRedis)


@driver_app.route(f"{API_NAME}/driver", methods=["GET"])
def list_drivers():
    """
    list_drivers --> list all the drivers
    Args:
    Return:
        drivers(dict): a list of drivers
    """
    drivers = [driver.to_dict() for driver in driver_manager.get_all()]
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
    driver = driver_manager.get_document(driver_id)
    return jsonify(driver.to_dict())


@driver_app.route(f"{API_NAME}/driver", methods=["POST"])
def save_driver():
    """
    save_driver --> save a driver
    Args:
    Return:
    """
    driver_dict = request.json
    driver = Driver.entity_from_dict(driver_dict)
    driver_manager.save_document(driver)

    return jsonify({"message": "The object was saved successfully"})


@driver_app.route(f"{API_NAME}/driver/<driver_id>", methods=["DELETE"])
def delete_driver(driver_id):
    """
    delete_driver --> delete a driver
    Args:
         driver_id(int): a driver identifier
    Return:
    """
    result_delete = driver_manager.delete(driver_id)
    return jsonify({"message": "The object was deleted successfully"})
