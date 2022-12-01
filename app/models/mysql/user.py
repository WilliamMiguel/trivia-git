from app.utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    scores = db.relationship('Score', backref = 'user', lazy = 'dynamic')
    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    # def __init__(self, **kwargs):
    #     super(User, self).__init__(**kwargs)
    #     if self.role is None:

    # def __init__(self, **kwargs):
    #     super(User, self).__init__()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
