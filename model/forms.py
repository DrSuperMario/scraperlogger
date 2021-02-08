from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class LoggerForm(FlaskForm):
    newest_button = SubmitField('Newest First')
    oldest_button = SubmitField('Oldest First')