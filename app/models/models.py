
from mongoengine import Document, StringField, EmailField, ReferenceField, DateTimeField
from flask_login import UserMixin
from datetime import datetime
from app import login_manager

class User(Document, UserMixin):
    meta = {'collection': 'users'}
    username = StringField(max_length=20, required=True, unique=True)
    email = EmailField(required=True, unique=True)
    image_file = StringField(max_length=100, default='default.jpg')
    password = StringField(required=True)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class UserSearch(Document):
    meta = {'collection': 'user_searches'}
    movie_title = StringField(max_length=255, required=True)
    user = ReferenceField(User, required=True, reverse_delete_rule=2)  # CASCADE
    timestamp = DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f"<UserSearch {self.movie_title} by User {self.user.id}>"

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects(id=user_id).first()
    except Exception:
        return None
