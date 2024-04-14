#!/usr/bin/python3

from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/api/v1')

from api.v1.views.terminals import *
from api.v1.views.agents import *
from api.v1.views.transactions import *
from api.v1.views.merchants import *
