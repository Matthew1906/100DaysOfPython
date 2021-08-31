# Import Modules
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators 
from flask_bootstrap import Bootstrap

# Create Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] ='well_this_is_just_for_learning'
Bootstrap(app)

# Create Form Class
class LoginForm(FlaskForm):
    email = StringField(label = 'Email',validators=[validators.DataRequired(), validators.length(max=30), validators.Email()])
    password = PasswordField(label='Password',validators=[validators.DataRequired(),validators.length(max=30)])
    submit = SubmitField(label='Log In')

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@admin.com' and login_form.password.data =='admin':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = login_form)

if __name__ == '__main__':
    app.run(debug=True)