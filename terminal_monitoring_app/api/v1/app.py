#!/home/zaya/.local/bin/python
"""#!/usr/bin/python3"""

import sys
import os
from flask_cors import CORS


current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
parent_directory = os.path.dirname(parent_directory)
print(parent_directory)
path_to_config = os.path.join(current_directory, '.gitignore', 'config.json')
sys.path.append(parent_directory)
from werkzeug.exceptions import Unauthorized
from flask import Flask, make_response, jsonify
from api.v1.views import views
from api.v1.utils import read_json

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.update(read_json(path_to_config))
app.secret_key = app.config['SECRET_KEY']
app.url_map.strict_slashes = False

@app.errorhandler(401)
def handle_unauthorized(error):
    print('error')
    return make_response(jsonify({'error': 'You no get permission, boss',
                    'status_code': 404}), 401)

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "you dey look for wetin no dey here oh. check your spelling, boss"}), 404)

@views.route('/')
def hello():
    return "hello\n"

app.register_blueprint(views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
