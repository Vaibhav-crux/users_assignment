from app.models.user import User
import logging
from app.utils.hash_password import hash_password
from app.utils.email_exist import is_email_exists

logger = logging.getLogger('app')

user_error = "User not found"

def get_all_users():
    """
    Fetch all users from the database and return a list of users without their passwords.
    """
    logger.info("Fetching all users")
    try:
        users = [user.to_dict() for user in User.objects]  # Convert all users to a dictionary format
        # Exclude the password field from the user data
        for user in users:
            user.pop('password', None)  # Remove the password field
        logger.debug(f"Fetched {len(users)} users")
        return users  # Return the list of users without passwords
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        raise ValueError("Error fetching users")  # Raise an error if something goes wrong


def get_user_by_id(user_id):
    """
    Fetch a single user by ID from the database and return the user's data without the password.
    """
    logger.info(f"Fetching user with ID: {user_id}")
    try:
        user = User.objects(id=user_id).first()  # Search for a user by ID
        if user:
            user_data = user.to_dict()  # Convert user to a dictionary
            user_data.pop('password', None)  # Remove the password field
            logger.debug(f"User found: {user_data}")
            return user_data  # Return the user data without the password
        logger.warning(f"User with ID: {user_id} not found")
        raise KeyError(user_error)  # Raise an error if the user is not found
    except Exception as e:
        logger.error(f"Error fetching user: {str(e)}")
        raise ValueError("Error fetching user by ID")  # Raise an error if something goes wrong


def create_user(data):
    """
    Create a new user after validating the email and hashing the password.
    """
    logger.info(f"Creating user with email: {data['email']}")
    try:
        # Check if the email already exists in the database
        if User.objects(email=data['email']):
            logger.warning(f"User creation failed. Email {data['email']} already exists.")
            raise ValueError("Email already exists")  # Raise an error if the email is taken

        # Hash the password before saving the user to the database
        hashed_password = hash_password(data['password'])
        user = User(name=data['name'], email=data['email'], password=hashed_password)  # Create new user object
        user.save()  # Save the user to the database
        
        # Convert the user object to a dictionary and exclude the password field
        user_data = user.to_dict()
        user_data.pop('password', None)  # Remove the password field
        logger.info(f"User created successfully with email: {data['email']}")
        return user_data  # Return the user data without the password
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        raise ValueError("Error creating user")  # Raise an error if something goes wrong


def update_user(user_id, data):
    """
    Update an existing user by ID. This will update the user's name and email, but not their password.
    """
    logger.info(f"Updating user with ID: {user_id}")
    try:
        # Find the user by ID
        user = User.objects(id=user_id).first()
        if not user:
            raise KeyError(user_error)  # Raise an error if the user is not found

        # Check if the new email is different and whether it's already in use
        new_email = data.get('email')
        if new_email and new_email != user.email:
            if User.objects(email=new_email):
                raise ValueError("Email already in use")  # Raise an error if the new email is taken

        # Update the user data in the database
        user.update(set__name=data.get('name', user.name), set__email=new_email if new_email else user.email)
        updated_user = User.objects(id=user_id).first()  # Fetch the updated user
        
        # Convert the updated user object to a dictionary and exclude the password field
        updated_user_data = updated_user.to_dict()
        updated_user_data.pop('password', None)  # Remove the password field
        logger.info(f"User with ID: {user_id} updated successfully")
        return updated_user_data  # Return the updated user data without the password
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")
        raise ValueError("Error updating user")  # Raise an error if something goes wrong


def delete_user(user_id):
    """
    Delete a user by ID from the database.
    """
    logger.info(f"Deleting user with ID: {user_id}")
    try:
        # Find the user by ID
        user = User.objects(id=user_id).first()
        if user:
            user.delete()  # Delete the user from the database
            logger.info(f"User with ID: {user_id} deleted successfully")
            return True  # Return True if the user was successfully deleted
        raise KeyError(user_error)  # Raise an error if the user is not found
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")
        raise ValueError("Error deleting user")  # Raise an error if something goes wrong
