#!/usr/bin/python3

import os
from api.v1.views import views
from flask import jsonify
from api.v1.authents import *
from api.v1.utils import *

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
path_to_terminals = os.path.join(parent_directory, 'files_storage', 'terminals.json')


@views.route('/terminals')
def all_terminals():
    agents = read_json("/home/zaya/my_project_backend_v1/flask_app/api/v1/files_storage/terminals.json")
    return agents


@views.route('/pterminals')
@auth.login_required
def all_pterminals():
    """    pterminals.append({'terminal_id': '97531',
                        'ptst': 'roadrun',
                        'merchant': 'spar'})"""
    return ("perminssion allowdd")

@views.route('/terminals/<string:id>')
@auth.login_required
def terminal(id):
    for terminal in terminals:
        if terminal['terminal_id'] == id:
            return jsonify(terminal)
    return(jsonify({'error': 'terminal not found'}))
