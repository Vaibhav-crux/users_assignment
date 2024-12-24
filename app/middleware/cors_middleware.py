from flask import Flask
from flask_cors import CORS

def enable_cors(app: Flask):
    """
    Enable Cross-Origin Resource Sharing (CORS) for the Flask application.
    """
    CORS(app, resources={r"/api/*": {"origins": "*"}})
