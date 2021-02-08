from db import db
from flask_login import UserMixin

class Admin(UserMixin, db.Model):

    __tablename__='user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    authenticated = db.Column(db.Boolean, default=False)


    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False