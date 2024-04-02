#!/usr/bin/python3
"""
perform CRUD operation on the users endpoints
of the airbnb application
"""
from api.v1.views import app_views, storage_type
from flask import jsonify, abort, request, make_response
from models.amenity import Amenity
from models.place import Place
from models import storage



@app_views.route('/places/<place_id>/amenities', methods=['GET'])
def list_place_amenities(place_id: str):
    """
    return a list of amenities from a place using place id
    """
    place = storage.get(Place, place_id)
    if place:
        lst = []
        if storage_type == 'db':
            lst = [place.to_dict() for place in place.amenities]
        else:
            amenities = place.amenity_ids
            lst = [storage.get(Amenity, amenity).to_dict() for amenity in amenities]
        return jsonify(lst), 200
    abort(404)

    
@app_views.route('/places/<place_id>/amenities/<amenity_id>')
def delete_place_amenities(place_id : str, amenity_id : str):
    """
    delete place amenities
    """
    place = storage.get(Place, place_id)
    if place:
        amenity = None
        if storage_type == 'db':
           amenity = place.amenities.id
        else:
            amenity =  [storage.get(Amenity, amenity) for amenity in place.amenity_ids if amenity == amenity_id]
            amenity = amenity[0] 
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'])
def create_place_amenities(place_id : str, amenity_id : str):
    """
    create place and amenity
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if storage_type == "db":
        if amenity in place.amenities:
            return make_response(jsonify(amenity.to_dict()), 200)
        place.amenities.append(amenity)
    else:
        if amenity_id in place.amenity_ids:
            return jsonify(amenity), 200
        place.amenity_ids.append(amenity_id)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 201)