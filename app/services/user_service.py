from app.models.user import User
from app.extensions.database import database

def get_all_users():
    return [user.to_dict() for user in User.query.all()]

def create_user(data):
    user = User(**data)
    database.session.add(user)
    database.session.commit()
    return user.to_dict()
