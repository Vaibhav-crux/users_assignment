from app.models.user import User
import logging
from app.utils.hash_password import hash_password
from app.utils.email_exist import is_email_exists

logger = logging.getLogger('app')

user_error = "User not found"

def get_all_users():
    logger.info("Fetching all users")
    try:
        users = [user.to_dict() for user in User.objects]
        # Exclude password from user data
        for user in users:
            user.pop('password', None)  # Remove the password field
        logger.debug(f"Fetched {len(users)} users")
        return users
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        raise ValueError("Error fetching users")


def get_user_by_id(user_id):
    logger.info(f"Fetching user with ID: {user_id}")
    try:
        user = User.objects(id=user_id).first()
        if user:
            user_data = user.to_dict()
            user_data.pop('password', None)
            logger.debug(f"User found: {user_data}")
            return user_data
        logger.warning(f"User with ID: {user_id} not found")
        raise KeyError(user_error)
    except Exception as e:
        logger.error(f"Error fetching user: {str(e)}")
        raise ValueError("Error fetching user by ID")


def create_user(data):
    """Create a new user after validating the email."""
    logger.info(f"Creating user with email: {data['email']}")
    try:
        if User.objects(email=data['email']):
            logger.warning(f"User creation failed. Email {data['email']} already exists.")
            raise ValueError("Email already exists")

        # Hash the password before saving
        hashed_password = hash_password(data['password'])
        user = User(name=data['name'], email=data['email'], password=hashed_password)
        user.save()
        
        user_data = user.to_dict()
        user_data.pop('password', None)  # Remove the password field
        logger.info(f"User created successfully with email: {data['email']}")
        return user_data
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        raise ValueError("Error creating user")


def update_user(user_id, data):
    logger.info(f"Updating user with ID: {user_id}")
    try:
        user = User.objects(id=user_id).first()
        if not user:
            raise KeyError(user_error)

        new_email = data.get('email')
        if new_email and new_email != user.email:
            if User.objects(email=new_email):
                raise ValueError("Email already in use")

        user.update(set__name=data.get('name', user.name), set__email=new_email if new_email else user.email)
        updated_user = User.objects(id=user_id).first()
        
        updated_user_data = updated_user.to_dict()
        updated_user_data.pop('password', None)  # Remove the password field
        logger.info(f"User with ID: {user_id} updated successfully")
        return updated_user_data
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")
        raise ValueError("Error updating user")


def delete_user(user_id):
    logger.info(f"Deleting user with ID: {user_id}")
    try:
        user = User.objects(id=user_id).first()
        if user:
            user.delete()
            logger.info(f"User with ID: {user_id} deleted successfully")
            return True
        raise KeyError(user_error)
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")
        raise ValueError("Error deleting user")
