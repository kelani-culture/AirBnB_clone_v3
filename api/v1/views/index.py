#!/usr/bin/python3
"""
flask route to status endpoint
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """return an ok status"""
    return jsonify({"status": "OK"})