#!/usr/bin/python3
"""
perform CRUD operation on the city endpoints
of the airbnb application
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.state import City, State
from models import storage



@app_views.route('/states/<state_id>/cities', methods=['GET'])
def retrieve_city_by_state(state_id):
    """
    retrieve all cities by the state id
    """
    state = storage.get(State,state_id)
    if state:
        cities = storage.all(City).values()
        cities_list = [city.to_dict() for city in cities if city.state_id == state.id]
        return jsonify(cities_list), 200
    abort(404)


@app_views.route('/cities/<city_id>', methods=['GET']) 
def retrieve_city(city_id):
    """
    retrieve city by id
    """
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    delete a city by id
    """
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """
    create a state by city
    """
    state = storage.get(State, state_id)
    if state:
        data = request.get_json()
        if data:
            if 'name' not in data:
                return jsonify('Missing a name'), 400
            
            city = City(**data)
            city.state_id = state_id
            city.save()
            city = storage.get(City, city.id)
            return jsonify(city.to_dict()), 201
        return jsonify('Not a Json'), 400
    abort(404)


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """
    update a city by the city od
    """
    city = storage.get(City, city_id)
    if city:
        data = request.get_json()
        if data:
            city.name = data['name']
            city.save()
            return jsonify(city.to_dict()), 200
        return ("Not a Json"), 400