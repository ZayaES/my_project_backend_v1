#!/usr/bin/python3
import sys
sys.path.append('/home/zaya/my_project_backend_v1/flask_app')
from werkzeug.exceptions import Unauthorized
from flask import Flask, make_response, jsonify
from api.v1.views import views

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
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
    return make_response(jsonify({'error': "Not found"}), 404)

@views.route('/')
def hello():
    return "hello\n"

app.register_blueprint(views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
