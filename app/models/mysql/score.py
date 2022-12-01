from app.utils.db import db
from datetime import datetime

class Score(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_score = db.Column(db.Integer)
    # timestamp = db.Column(db.Datetime, index = True, default = datetime.utcnow)