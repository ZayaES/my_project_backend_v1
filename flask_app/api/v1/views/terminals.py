#!/usr/bin/python3

from api.v1.views import views
from flask import jsonify


terminals = [{'terminal_id': '12345',
                'ptst': 'posman',
                'merchant':'shoprite'},
            {'terminal_id': '54321',
                'ptst': 'roadrun',
                'merchant': 'uber'},
            {'terminal_id': '02468',
                'ptst': 'posman',
                'merchant': 'spar'}]

@views.route('/terminals')
def terminals():
    return (terminals)
