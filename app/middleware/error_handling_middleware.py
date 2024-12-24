from flask import jsonify
import logging

# Get logger
logger = logging.getLogger('app')

def handle_error(error):
    """Handle various types of errors."""
    
    # Handle specific error codes or general exceptions
    if isinstance(error, KeyError):
        logger.error(f"KeyError occurred: {str(error)}")
        return jsonify({"error": "Key not found"}), 400
    elif isinstance(error, ValueError):
        logger.error(f"ValueError occurred: {str(error)}")
        return jsonify({"error": "Invalid value provided"}), 400
    elif isinstance(error, TypeError):
        logger.error(f"TypeError occurred: {str(error)}")
        return jsonify({"error": "Type mismatch"}), 400
    elif hasattr(error, 'code') and error.code == 404:
        logger.error(f"404 Not Found: {str(error)}")
        return jsonify({"error": "Resource not found"}), 404
    elif hasattr(error, 'code') and error.code == 500:
        logger.error(f"500 Internal Server Error: {str(error)}")
        return jsonify({"error": "Internal server error. Please try again later"}), 500
    else:
        # Generic error handling for unhandled exceptions
        logger.error(f"Unhandled error: {str(error)}")
        return jsonify({"error": "Something went wrong. Please try again later."}), 500

def init_error_handling(app):
    """Initialize error handling middleware."""
    app.register_error_handler(Exception, handle_error)  # Catch all unhandled exceptions
    app.register_error_handler(404, handle_error)  # Catch 404 errors
    app.register_error_handler(500, handle_error)  # Catch 500 errors
