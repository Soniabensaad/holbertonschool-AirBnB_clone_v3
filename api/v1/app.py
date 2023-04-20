#!/usr/bin/python3
"""create a variable app, instance of Flask
"""
import os
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

"""
create a variable app, instance of Flask
import storage from models
import app_views from api.v1.views
register the blueprint app_views to your Flask ins
inside if __name__ == "__main__":, run your Flask server (variable app) with:
host = environment variable HBNB_API_HOST or 0.0.0.0 if not defined
port = environment variable HBNB_API_PORT or 5000 if not defined
threaded=True
"""

# Create Flask instance
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register blueprints
app.register_blueprint(app_views)

# Teardown app context
@app.teardown_appcontext
def teardown_app_context(exception):
    
    storage.close()

if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = os.environ.get("HBNB_API_PORT", 5000)

   
    app.run(host=host, port=port, threaded=True)
