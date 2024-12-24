import mongoengine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize MongoDB connection
def init_db(app):
    mongoengine.connect(
        host=os.getenv('MONGO_URI'),  # Use the MONGO_URI from .env
        alias='default'  # The default alias for the connection
    )
    app.logger.info("MongoDB connected successfully!")
