import os

from flask import Flask, redirect, flash, url_for
from flask.globals import request
from flask.templating import render_template
from flask_login import LoginManager, login_manager
from werkzeug.security import check_password_hash

from model.loggerCleaner import load_log_from_file as log
from model.loggerCleaner import add_html_tolog as aht
from model.forms import LoginForm
from model.admin import Admin

from db import db


app = Flask(__name__)
login_manager = LoginManager()
app.config['SECRET_KEY'] = '45Us6Bp8c5f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_BINDS'] = {'user':"sqlite:///users.db"}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


# @app.route('/', methods=['GET'])
# def home():
#     log_data = log(filename='temp/scraper.log')
#     data = aht(log_data, tag='li',style='list-group-item')
#     #breakpoint()

#     return render_template('index.html', data=data)
db.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
    return Admin.query.get(user_id)

@app.route('/', methods=['GET','POST'])
def login():

    error = None

    # if(request.method == 'POST'):
        
    #     if((request.form['username'] != 'admin') and (request.form['inputPassword'] != 'admin')):
    #         error = 'invalid Username and Password'
    #         flash('Invalid Username or Password')
    #     else:
    #         log_data = log(filename='temp/scraper.log')
    #         data = aht(log_data, tag='li',style='list-group-item')
    #         return render_template('home.html', data=data) 

    form = LoginForm()
    #breakpoint()
    if((request.method == 'POST') and (form.validate)):
        user = Admin.query.filter_by(username=form.username.data).first()
        if((not user) or (not check_password_hash(user.password, form.password.data))):
            print("NO match for the old guy")
        else:
            log_data = log(filename='temp/scraper.log')
            data = aht(log_data, tag='li',style='list-group-item')
            return render_template('home.html', data=data) 
        
 
    return render_template('index.html',form=form, title = error if error != None else "happy hunting" )    

# @app.before_first_request
# def first_request():
#     db.create_all(bind='user')

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5050, debug=True)

