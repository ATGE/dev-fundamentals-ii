"""
Transportation company API.
"""
from flask import (
    Flask,
    jsonify,
)

from truck_routes import truck_app
from driver_routes import driver_app
from const import API_NAME

app = Flask(__name__)
app.register_blueprint(truck_app)
app.register_blueprint(driver_app)


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
