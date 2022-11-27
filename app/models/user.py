from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, name, lastname, username, email, password, isAdmin=False):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.isAdmin = isAdmin

    def to_json(self):
        return {
            'name': self.name,
            'lastname': self.lastname,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'isAdmin': self.isAdmin
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
