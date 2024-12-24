from flask import Blueprint, request, jsonify
from app.services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user
import logging

# Get logger instance for logging messages
logger = logging.getLogger('app')

# Create a Blueprint instance for user-related routes
user_bp = Blueprint('user_routes', __name__)

# Route to fetch all users
@user_bp.route('/users', methods=['GET'])
def list_users():
    """
    Fetches all users from the database and returns them in the response.
    """
    logger.info("Received request to fetch all users")
    try:
        users = get_all_users()  # Call service to get all users
        return jsonify(users), 200  # Return the users as JSON with a 200 OK status
    except Exception as e:
        logger.error(f"Error in fetching users: {str(e)}")  # Log error if fetching fails
        return jsonify({"error": "Error fetching users"}), 500  # Return error if something goes wrong


# Route to fetch a user by their ID
@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Fetch a single user by their ID and return the user data.
    """
    logger.info(f"Received request to fetch user with ID: {user_id}")
    try:
        user = get_user_by_id(user_id)  # Call service to get user by ID
        return jsonify(user), 200  # Return the user data as JSON with a 200 OK status
    except Exception as e:
        logger.error(f"Error in fetching user by ID {user_id}: {str(e)}")  # Log error if fetching fails
        return jsonify({"error": "Error fetching user"}), 500  # Return error if something goes wrong


# Route to create a new user
@user_bp.route('/users', methods=['POST'])
def add_user():
    """
    Create a new user with the provided data.
    """
    data = request.json  # Get the request body as JSON
    logger.info(f"Received request to create a new user with email: {data['email']}")

    try:
        # Validate that the required fields (name, email, password) are provided
        if not data.get('name') or not data.get('email') or not data.get('password'):
            logger.warning("Name, email, and password are required")  # Log a warning if any field is missing
            return jsonify({"error": "Name, email, and password are required"}), 400  # Return error response with a 400 Bad Request status

        # Attempt to create the user using the service
        user = create_user(data)
        return jsonify(user), 201  # Return the created user data with a 201 Created status
    except ValueError as e:
        logger.warning(f"Error creating user: {str(e)}")  # Log a warning if user creation fails due to validation error
        return jsonify({"error": str(e)}), 400  # Return the error message with a 400 Bad Request status
    except Exception as e:
        logger.error(f"Error in user creation: {str(e)}")  # Log error for any other failures
        return jsonify({"error": "Error creating user"}), 500  # Return error response with a 500 Internal Server Error status


# Route to update an existing user
@user_bp.route('/users/<user_id>', methods=['PUT'])
def modify_user(user_id):
    """
    Update an existing user's details (name, email) by their ID.
    """
    data = request.json  # Get the request body as JSON
    logger.info(f"Received request to update user with ID: {user_id}")

    try:
        # Attempt to update the user using the service
        updated_user = update_user(user_id, data)
        return jsonify(updated_user), 200  # Return the updated user data with a 200 OK status
    except ValueError as e:
        logger.warning(f"Error updating user: {str(e)}")  # Log a warning if user update fails due to validation error
        return jsonify({"error": str(e)}), 400  # Return the error message with a 400 Bad Request status
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")  # Log error for any other failures
        return jsonify({"error": "Error updating user"}), 500  # Return error response with a 500 Internal Server Error status


# Route to delete a user by their ID
@user_bp.route('/users/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    """
    Delete a user by their ID.
    """
    logger.info(f"Received request to delete user with ID: {user_id}")
    try:
        deleted = delete_user(user_id)  # Call service to delete the user by ID
        if deleted:
            return jsonify({"message": "User deleted successfully"}), 200  # Return success message with a 200 OK status
        return jsonify({"error": "User not found"}), 404  # Return error if user not found, with a 404 Not Found status
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")  # Log error if deletion fails
        return jsonify({"error": "Error deleting user"}), 500  # Return error response with a 500 Internal Server Error status
