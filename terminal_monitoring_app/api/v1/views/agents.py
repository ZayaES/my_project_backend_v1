#!/usr/bin/python3

import os
from api.v1.views import views
from api.v1.utils import *
from api.v1.authents import *
from flask import jsonify

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
path_to_agents = os.path.join(parent_directory, 'files_storage', 'agents.json')


@views.route('/agents', defaults={'count': 10})
@views.route('/agents=<int:count>')
#@auth.login_required
@login_required
def agents_by_counts(count):
    agents = read_json(path_to_agents)
    return [agent for agent in agents[:count]]


@views.route('/agents/<string:unq_field>')
@login_required
def agent_by_code(unq_field):
    agents = read_json(path_to_agents)
    if (len(unq_field) < 11):
        for agent in agents:
            if(agent['Code'] == unq_field):
                return agent
            else:
                continue
    if (len(unq_field) >= 11):
        if ('@' in unq_field):
            for agent in agents:
                if(agent['Email'] == unq_field):
                    return agent
                else:
                    continue
        else:
            for agent in agents:
                if(agent['Phone Number'] == unq_field):
                    return agent
                else:
                    continue
    return jsonify({"error": "no agent with code {}".format(unq_field)})
