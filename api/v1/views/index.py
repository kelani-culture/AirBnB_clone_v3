#!/usr/bin/python3
"""flask route to status endpoint"""

from api.v1.views import app_views
from flask import jsonify
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.user import User
from models import storage

OBJECTS = [
    Amenity, Place, Review,
    City, State, User
]
@app_views.route('/status', methods=['GET'])
def status():
    """return an ok status"""
    return jsonify({"status": "OK"})

    
    
@app_views.route('/stats', methods=['GET'])
def object_stats():
    """get a stat on all objects"""
    obj_stats = {}
    for val in OBJECTS:
        obj_stats[val.__tablename__] = storage.count(val)
    
    return jsonify(obj_stats)