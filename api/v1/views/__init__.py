#!/usr/bin/python3
"""Blueprint for the flask application endpoints"""
from os import getenv
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

storage_type = getenv('HBNB_TYPE_STORAGE')
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.index import *