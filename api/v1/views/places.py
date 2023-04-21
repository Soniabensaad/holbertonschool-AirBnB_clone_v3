#!/usr/bin/python3
"""
Same as State, create a new view for City
objects that handles all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def place_c(city_id):
    list = []
    states = storage.all(City)
    id = f"City.{city_id}"
    if id  not in states:
        abort(404)
    city = storage.all(Place).values()
    for s in city:
        sity = s.to_dict()
        if "city_id" in sity:
            if sity["city_id"] == city_id:
                list.append(s.to_dict())
    return jsonify(list)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def place_p(place_id):
    """Retrieves a city object"""
    city = storage.all(Place)
    id = f"Place.{place_id}"
    if id  not in city:
        abort(404)
    c = city[id]
    return jsonify(c.to_dict())


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete(place_id):
    city = storage.all(Place)
    id = f"Place.{place_id}"
    if id not in city:
        abort(404)
    d = city[id]
    storage.delete(d)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def post(city_id):
    states = storage.all(City)
    id = f"City.{city_id}"
    if id not in states:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    if 'name' not in data:
        abort(400, 'Missing name')
    user = storage.all(User)
    id = f"User.{data['user_id']}"
    if id not in user:
        abort(404)
    city = Place(**data)
    storage.new(city)
    storage.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def place5(place_id):
    city = storage.all(Place)
    id = f"place.{place_id}"
    if id not in city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    p = city[id]
    x = p.__dict__
    for i in data:
        if i not in ["id", "created_at",
                     "updated_at"]:
            x[i] = data[i]
    storage.save()
    return jsonify(x.to_dict()), 200
