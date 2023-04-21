#!/usr/bin/python3
"""
Create a new view for State objects that handles
all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State
import models


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def status():
    list = []
    states = storage.all(State).values()
    for state in states:
        list.append(state.to_dict())
    return jsonify(list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    states = storage.all(State)
    id = f"State.{state_id}"
    if id not in states:
        abort(404)
    state = states[id]
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    states = storage.all(State)
    id = f"State.{state_id}"
    if id not in states:
        abort(404)
    state = states[id]
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post():
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    state = State(name=data['name'])
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put(state_id):
    data = request.get_json()
    states = storage.all(State)
    id = f"State.{state_id}"
    if id not in states:
        abort(404)
    if not data:
        abort(400, "Not a JSON")
    state = states[id]
    state_d = state.__dict__
    for a in data:
        if a not in ["id", "created_at",
                     "updated_at"]:
            state_d[a] = data[a]
        storage.save()
    return jsonify(state_d, 200)
    
