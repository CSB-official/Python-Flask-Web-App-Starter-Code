from app import db
from flask_login import UserMixin
import datetime

class User(UserMixin, db.Model):
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key = True)

    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    user_type = db.Column(db.String(30))

    email = db.Column(db.String(60), unique = True)
    phone_number = db.Column(db.String(30))
    password = db.Column(db.String(30))

    most_recent_login = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    total_num_logins = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)