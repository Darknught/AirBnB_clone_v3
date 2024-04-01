#!/usr/bin/python3
"""Init file"""
from .places import *
from .users import *
from .amenities import *
from .cities import *
from .states import *
from .index import *
from flask import Blueprint

app_views = Blueprint('api_v1', __name__, url_prefix='/api/v1')
