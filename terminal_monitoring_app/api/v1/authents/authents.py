#!/usr/bin/python3

import os
from api.v1.views import views
from flask_httpauth import HTTPBasicAuth
from werkzeug.exceptions import Unauthorized
from api.v1.utils import read_json
from flask import Flask, request, jsonify, session, Response, make_response
from functools import wraps


current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
path_to_admins = os.path.join(parent_directory, 'files_storage', 'admins.json')
auth = HTTPBasicAuth()


def login_required(f):
    """ session based authentication check
        makes sure user is login/in session before granting access
        to function decorated with it

        args: f - the function it is wrapped in
        returns: decoraged function with checks for user in session
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """ checks if logged in is in session  which has been
            set at successful log in
            args - *args and **kwargs - possible argument inherited from f
            returns - 401 if unsuccessful
                    - result of function f() if successful
        """

        if 'logged_in' not in session:
            return jsonify({'message': 'You no get access boss'}), 401
        return f(*args, **kwargs)
    return decorated_function


@auth.verify_password
def verify_password(username, password):
    admins = read_json(path_to_admins)
    for admin in admins:
        if admin['username'] == username and admin['password'] == password:
            return username

@views.route('/login', methods=['POST'])
def login():
    """ Login authentication - user credentials
        return - json formatted output which contains
                 result (access given or granted) and role
    """

    data = request.form
    username = data['username']
    password =data['password']
    admins = read_json(path_to_admins)
    for admin in admins:
        if (admin['username'] == username and admin['password'] == password):
            session['logged_in'] = True
            session['username'] = username
            return jsonify({"result": admin}), 200
        else:
            continue
    return jsonify({"result": "login unsuccessful"}), 401

@views.route('/logout', methods=['POST'])
@login_required
def logout():
    response = Response()
    session.clear()
    #print(request.cookie)
    response.set_cookie('session', '', expires=0)
    response = make_response(jsonify({'message': 'Logout successful'}), 200)
    return response


@views.errorhandler(Unauthorized)
def handle_unauthorized(error):
    print('error')
    return jsonify({'error': 'You no get permission, boss',
                     'status_code': 404})
