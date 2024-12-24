import os
from dotenv import load_dotenv
from flask import Flask
from app.config.database import init_db
from app.routes.user_routes import user_bp
from app.routes.root_routes import root_bp
from app.middleware.cors_middleware import enable_cors
from app.middleware.error_handling_middleware import init_error_handling
from app.config.logging_config import setup_logging

# Load environment variables from the .env file
load_dotenv()

# Setup logging
logger = setup_logging()

def create_app():
    app = Flask(__name__)

    # Set up MongoDB connection string from environment variables
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    
    # Initialize the database
    init_db(app)
    
    # Enable CORS middleware
    enable_cors(app)
    
    # Register blueprints
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(root_bp)  # Register root route blueprint
    
    # Initialize error handling
    init_error_handling(app)

    logger.info("Application started successfully")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
