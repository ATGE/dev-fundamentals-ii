"""
Transportation company API.
"""
from flask import (
    Flask,
    jsonify,
)

from truck_delivery_atge.api.views.driver_routes import driver_app
from truck_delivery_atge.api.views.client_routes import client_app
from truck_delivery_atge.shared_core.const import API_NAME

app = Flask(__name__)
app.register_blueprint(driver_app)
app.register_blueprint(client_app)


@app.route("/", methods=["GET"])
def health_check():
    """
    health check
    """
    return f"Transportation company API: {API_NAME}"


@app.errorhandler(404)
def resource_not_found(_error):
    """
    resource not found
    """
    return jsonify(error=str(_error)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True,
            use_reloader=True,
            port=5000)
