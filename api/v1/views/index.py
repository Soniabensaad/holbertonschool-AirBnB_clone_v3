#!/usr/bin/python3
"""import app_views from api.v1.views
"""
from api.v1.views import app_views
from flask import jsonify
"""
import app_views from api.v1.views
create a route /status on the object app_views that returns a JSON
"""
@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify(status="OK")
