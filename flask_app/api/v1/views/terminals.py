#!/usr/bin/python3

from api.v1.views import views
from flask import jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = [{'username': 'zaya',
            'passwd': 'tutu'},
        {'username': 'joseph',
            'passwd': 'josh'}]

terminals = [{'terminal_id': '12345',
                'ptst': 'posman',
                'merchant':'shoprite'},
            {'terminal_id': '54321',
                'ptst': 'roadrun',
                'merchant': 'uber'},
            {'terminal_id': '02468',
                'ptst': 'posman',
                'merchant': 'spar'}]

pterminals = terminals


@auth.verify_password
def verify_password(username, passwd):
    for user in users:
        if user['username'] == username and user['passwd'] == passwd:
            return True
    return False

@views.route('/terminals')
def all_terminals():
    return terminal


@views.route('/pterminals')
@auth.login_required
def all_pterminals():
    pterminals.append({'terminal_id': '97531',
                        'ptst': 'roadrun',
                        'merchant': 'spar'})
    return (pterminals)
