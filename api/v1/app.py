#!/usr/bin/python3
import os
from flask import Flask
from models import storage
from api.v1.views import app_views

# Create Flask instance
app = Flask(__name__)

# Register blueprints
app.register_blueprint(app_views)

# Teardown app context
@app.teardown_appcontext
def teardown_app_context(error):
    
    storage.close()

if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = os.environ.get("HBNB_API_PORT", 5000)

   
    app.run(host=host, port=port, threaded=True)
