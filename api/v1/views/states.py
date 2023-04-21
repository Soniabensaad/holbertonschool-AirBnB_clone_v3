#!/usr/bin/python3
"""Create a new view for State objects"""

from api.v1.views import app_views
from flask import Flask, jsonify,  request, abort
from models import  storage
from models.state import State
import models

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def getstate():
    """retrieve all:"""
    state_list = []
    state_obj = storage.all("State")
    for obj in state_obj.values():
        state_list.append(obj.to_json())

    return jsonify(state_list)
    
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get(self, state_id):
    """retrieve one object:"""
    if state_id:
        state = State.query.get_or_404(state_id)
        return jsonify(state.to_dict())
    else:
        states = State.query.all()
        return jsonify([state.to_dict() for state in states])

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete(self, state_id):
    """delete one by id"""
    state = storage.get("State", str(state_id))
    if state is None:
        abort(404)
    
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
    
