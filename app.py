import os

from flask import (
                    Flask, 
                    redirect, 
                    flash, 
                    url_for
                )
from flask.globals import request
from flask.templating import render_template
from flask_login import (
                         LoginManager, 
                         login_manager, 
                         login_user, 
                         logout_user 
                    )
from flask_login.utils import login_required
from flask_wtf.form import _is_submitted
from werkzeug.security import check_password_hash

from model.loggerCleaner import LoadLog
from model.forms import LoginForm, LoggerForm
from model.admin import Admin

from db import db


app = Flask(__name__)
login_manager = LoginManager()
app.config['SECRET_KEY'] = '45Us6Bp8c5f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


db.init_app(app)
login_manager.init_app(app)

load_log = LoadLog()

@login_manager.user_loader
def user_loader(user_id):
    return Admin.query.filter_by(username=user_id).first()

@app.route('/', methods=['GET','POST'])
def login():

    error = None

    form = LoginForm()
    #breakpoint()
    if((request.method == 'POST') and (form.validate)):
        user = Admin.query.filter_by(username=form.username.data).first()
        if((not user) or (not check_password_hash(user.password, form.password.data))):
            flash("NO match for the old guy")
        else:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            #breakpoint()
            return redirect(url_for('home'))
            
        
 
    return render_template('index.html',form=form, title = error if error != None else "happy hunting" )    

@app.route('/home', methods=['GET','POST'])
@login_required
def home():
    form = LoggerForm()
    data = load_log.add_html_tolog(
                                        tag='li',
                                        style='list-group-item', 
                                        oldest_first=False
                                    )

    if((request.method == 'POST') and (form.newest_button.data)):
        data = load_log.add_html_tolog( 
                                        tag='li',
                                        style='list-group-item', 
                                        oldest_first=False
                                    )
        return render_template('home.html',form=form, data=data)

    elif((request.method == 'POST') and (form.oldest_button.data)):

        data = load_log.add_html_tolog(
                                        tag='li',
                                        style='list-group-item', 
                                        oldest_first=True
                                    )

        return render_template('home.html',
                                form=form, 
                                data=data
                            )

    return render_template('home.html',form=form, data=data) 

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__=="__main__":

    with app.app_context():
        db.create_all()
    
    app.run(port=5050, debug=True)

