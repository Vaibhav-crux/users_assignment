from app.models.user import User

def is_email_exists(email):
    """Check if the given email already exists in the database."""
    return User.objects(email=email).first() is not None
