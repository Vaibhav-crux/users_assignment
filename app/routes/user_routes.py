from flask import Blueprint, request, jsonify
from app.services.user_service import (
    get_all_users, get_user_by_id, create_user, update_user, delete_user
)
import logging

# Get logger
logger = logging.getLogger('app')

user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/users', methods=['GET'])
def list_users():
    logger.info("Received request to fetch all users")
    try:
        users = get_all_users()
        return jsonify(users), 200
    except Exception as e:
        logger.error(f"Error in fetching users: {str(e)}")
        return jsonify({"error": "Error fetching users"}), 500

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    logger.info(f"Received request to fetch user with ID: {user_id}")
    try:
        user = get_user_by_id(user_id)
        return jsonify(user), 200
    except Exception as e:
        logger.error(f"Error in fetching user by ID {user_id}: {str(e)}")
        return jsonify({"error": "Error fetching user"}), 500

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    logger.info(f"Received request to create a new user with email: {data['email']}")
    
    try:
        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('password'):
            logger.warning("Name, email, and password are required")
            return jsonify({"error": "Name, email, and password are required"}), 400

        # Attempt to create the user
        user = create_user(data)
        return jsonify(user), 201
    except ValueError as e:
        logger.warning(f"Error creating user: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Error in user creation: {str(e)}")
        return jsonify({"error": "Error creating user"}), 500

@user_bp.route('/users/<user_id>', methods=['PUT'])
def modify_user(user_id):
    data = request.json
    logger.info(f"Received request to update user with ID: {user_id}")
    
    try:
        updated_user = update_user(user_id, data)
        return jsonify(updated_user), 200
    except ValueError as e:
        logger.warning(f"Error updating user: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")
        return jsonify({"error": "Error updating user"}), 500

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    logger.info(f"Received request to delete user with ID: {user_id}")
    try:
        deleted = delete_user(user_id)
        if deleted:
            return jsonify({"message": "User deleted successfully"}), 200
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")
        return jsonify({"error": "Error deleting user"}), 500
