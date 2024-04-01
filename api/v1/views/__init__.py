#!/usr/bin/python3
"""Init file"""
from flask import Blueprint
from .index import *
from .states import *
from .cities import *
from .amenities import *
from .users import *

app_views = Blueprint('api_v1', __name__, url_prefix='/api/v1')
