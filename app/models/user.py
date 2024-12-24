import uuid
from mongoengine import Document, StringField

class User(Document):
    id = StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)

    # Convert the object to dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
