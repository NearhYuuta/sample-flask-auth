from database import db
from flask_login import UserMixin
class User(db.Model, UserMixin):
    #id (int), username (string), password (string), role (text)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')