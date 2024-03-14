#!/usr/bin/python3
import sys
sys.path.append('/home/zaya/my_project_backend_v1/flask_app')
from flask import Flask
from api.v1.views import views

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False

@views.route('/')
def hello():
    return "hello\n"

app.register_blueprint(views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
