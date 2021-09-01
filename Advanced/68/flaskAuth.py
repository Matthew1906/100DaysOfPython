# Import Modules
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Configure Application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-auth'

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# Configure Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        new_user = User(
            email = request.form['email'],
            password = generate_password_hash(request.form['password'],'pbkdf2:sha256', 8),
            name = request.form['name']
        )
        if User.query.filter_by(email=request.form['email']).first():
            flash("Email already exist!")
        else:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return render_template('secrets.html', user=new_user)
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        logged_user = User.query.filter_by(email=request.form['email']).first()
        if check_password_hash(logged_user.password, request.form['password']):
            login_user(logged_user)
            return render_template('secrets.html', user=logged_user)
        else:
            flash("Wrong Email or Password!")
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
