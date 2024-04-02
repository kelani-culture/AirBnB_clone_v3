#!/usr/bin/python3
"""Wrapper of AirBnB web app built using Flask"""

import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(exc):
    """close the storage session"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """return a 404 not found error for
       incorrect endpoints""" 
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host =  os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
