#!/usr/bin/python3
"""
create a variable app, instance of Flask
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)

@app_views.route('/status')
def status():
    return jsonify(status="OK")


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


"""
create a variable app, instance of Flask
"""




if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
