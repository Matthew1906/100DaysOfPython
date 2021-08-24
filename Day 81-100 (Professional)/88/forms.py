# Import modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

class LoginForm(UserForm):
    submit = SubmitField("Login")

class RegisterForm(UserForm):
    submit = SubmitField("Register")
