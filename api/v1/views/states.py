#!/usr/bin/python3
"""
perform CRUD operation on the state endpoints
of the airbnb application
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.state import State
from models import storage



@app_views.route('/states', methods=['GET'])
def all_states():
    """
    retrieve all state
    """
    all_states = storage.all(State)
    if all_states:
        state_list = []
        for value in all_states.values():
            state_list.append(value.to_dict())
        return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def retrieve_state(state_id):
    """
    retrieve state object by id
    """
    instance = storage.get(State, state_id)
    if instance:
        dict_instance = instance.to_dict()
        return jsonify(dict_instance)
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """
    Delete a state by id
    """
    get_state = storage.get(State, state_id)
    if get_state:
        storage.delete(get_state)
        storage.save()
        return jsonify({}), 200 
    abort(404)

    
@app_views.route('/states/', methods=['POST'])
def create_state():
    """
    perform a post request on the state object
    """
    data =  request.get_json()
    if data:
        if 'name' in data.keys():
            new_state = State(name=data['name'])
            new_state.save()
            get_state = storage.get(State, new_state.id)
            return jsonify(get_state.to_dict()), 201
        return jsonify("Missing a name"), 400
    return jsonify("Not a Json"), 400



@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """
    update a state by it's id
    """
    get_state = storage.get(State, state_id)
    if get_state:
        data = request.get_json()
        if data:
            get_state.name = data['name']
            get_state.save()
            return jsonify(get_state.to_dict()), 200
        return jsonify("Not a json"), 400
    abort(404)