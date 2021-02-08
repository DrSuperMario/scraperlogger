from werkzeug.security import generate_password_hash
import argparse

from db import db
from app import app

from model.admin import Admin

def make_admin(username, password):

    __tablename__='user'

    password_gen = generate_password_hash(password, method='sha256')
    
    with app.app_context():
        add_admin = Admin(username=username, password=password_gen)
        db.session.add(add_admin)
        db.session.commit()
        db.session.close()

if __name__=="__main__":
    arguments = argparse.ArgumentParser(description="Hash Admin passwd")
    arguments.add_argument('--username', help='Add username to DB')
    arguments.add_argument('--password', help='Add password to DB')
    args = arguments.parse_args()
    if((not args.username) or (not args.password)):
        print("Aruments --username and --password must be added")
    else:    
        make_admin(args.username, args.password)
        print("User added to db")
