#!/usr/bin/python3
"""Index file"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieve the number of each object by type."""
    classes = [User, City, Place, Review, State, Amenity]
    stats = {}
    for cls in classes:
        count = storage.count(cls)
        stats[cls.__name__] = count
    return jsonify(stats)
