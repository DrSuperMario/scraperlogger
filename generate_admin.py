from werkzeug.security import generate_password_hash

from db import db
from app import app

from model.admin import Admin

def make_admin():

    __tablename__='user'

    username = "admin"
    password = "admin"
    password_gen = generate_password_hash(password, method='sha256')
    
    with app.app_context():
        add_admin = Admin(username=username, password=password_gen)
        db.session.add(add_admin)
        db.session.commit()
        db.session.close()

if __name__=="__main__":
    make_admin()