#!/usr/bin/python3
"""
create a variable app, instance of Flask
"""
from flask import Blueprint
from api.v1.views.index import *
"""mport Blueprint from flask doc"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
