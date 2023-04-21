#!/usr/bin/python3
"""
Create a new view for State objects that handles
all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State, City
import models


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def status():
    list = []
    cities = storage.all(City).values()
    for city in cities:
        list.append(city.to_dict())
    return jsonify(list)


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_state(state_id, city_id):
    """Retrieves a State object"""
    states = storage.all(State)
    id_s = f"State.{state_id}"
    cities = storage.all(City)
    id_c = f"City.{city_id}"
    if id_s not in states:
        abort(404)
    if id_c not in states:
        abort(404)
    city = cities[id_c]
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(city_id):
    cities = storage.all(City)
    id = f"State.{city_id}"
    if id not in cities:
        abort(404)
    city = cities[id]
    storage.delete(city)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post():
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    state = City(name=data['name'])
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put(state_id):
    data = request.get_json()
    states = storage.all(City)
    id = f"State.{state_id}"
    if id not in states:
        abort(404)
    if not data:
        abort(400, "Not a JSON")
    state = states[id]
    s=state.__dict__
    for a in data:
        if a not in ["id", "state_id", "created_at",
                     "updated_at"]:
            s[a] = data[a]
        storage.save()
    return jsonify(s, 200)
    
