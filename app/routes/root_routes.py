from flask import Blueprint, jsonify

# Create a Blueprint for the root route
root_bp = Blueprint('root_routes', __name__)

@root_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Server is running successfully!"}), 200
