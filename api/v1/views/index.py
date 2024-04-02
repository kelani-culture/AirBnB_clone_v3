#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
"""
flask route to status endpoint
"""


@app_views.route('/status', methods=['GET'])
def status():
    """return an ok status"""
    return jsonify({"status": "OK"})