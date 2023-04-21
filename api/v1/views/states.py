#!/usr/bin/python3
"""Create a new view for State objects"""

from api.v1.views import app_views
from flask import Flask, jsonify,  request
from models import storage
from models.state import State
import models
@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get(self, state_id):
        """retrieve one object:"""
        if state_id:
            state = State.query.get_or_404(state_id)
            return jsonify(state.to_dict())
        else:
            states = State.query.all()
            return jsonify([state.to_dict() for state in states])
       
