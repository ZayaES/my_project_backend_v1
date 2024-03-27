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
@login_required
def all_terminals():
    count = request.args.get('count', 20, type=int)
    offset = request.args.get('offset', 0, type=int)
    terminals = read_json(path_to_terminals)
    return terminals[offset:offset + count]


@views.route('/terminals/<string:id>')
@login_required
def terminal(id):
    terminals = read_json(path_to_terminals)
    for terminal in terminals:
        if terminal['terminal_id'] == id:
            return jsonify(terminal)
    return(jsonify({'error': 'terminal with id {} not found'.format(id)}))
