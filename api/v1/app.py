#!/usr/bin/python3
"""Module that defines the app"""
from flask import Flask, jsonify
import os
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception=None):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return a custom message for 404 errors."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)