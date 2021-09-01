# Import modules
## Flask App
from flask import Flask, render_template, request, redirect, url_for, flash
## Forms
from forms import LoginForm, RegisterForm
## Database Management
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
## Login Management
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
## Environment Variables management
from dotenv import load_dotenv
from os import getenv
## Datetime Management
from datetime import datetime

# Load Environment variables
load_dotenv()

# Create App
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# Connect to Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Config Database
if getenv('DATABASE_URL') == None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
else: 
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL').replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database tables
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    todolists = relationship("ToDoList", back_populates='author')

class ToDoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates='todolists')
    activities = relationship("Activity", back_populates='parent_list')

class Activity(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    color = db.Column(db.String(255))
    star = db.Column(db.Boolean)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'))
    parent_list = relationship("ToDoList", back_populates='activities')

# Paste uncommented extra code snippet here!

# Default loading user function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    # If user is logged in, then the page will look for existing lists
    if current_user.is_authenticated:
        todolist = ToDoList.query.filter_by(author=current_user).first()
        if todolist is None:
            date = datetime.now().strftime("%d/%m/%Y")
            todolist = ToDoList(name=f'My Todolist {date}', author=current_user)
            db.session.add(todolist)
            db.session.commit()
    # Else it wil show a temporary list
    else:
        todolist = []
    return render_template('index.html', todo=todolist)

@app.route('/todolist/<int:id>')
@login_required
def show_list(id):
    todolist = ToDoList.query.filter_by(id=id).first()
    return render_template('index.html', todo=todolist)

# CRUD Todolist
## Add new todolist
@app.route('/todolist/add')
@login_required
def add_list():
    date = datetime.now().strftime("%d/%m/%Y")
    todolist = ToDoList(name=f'My Todolist {date}', author=current_user)
    db.session.add(todolist)
    db.session.commit()
    return render_template('index.html', todo=todolist)

## Update todolist name
@app.route('/todolist/<int:id>/edit', methods=['POST'])
@login_required
def edit_list(id):
    todolist = ToDoList.query.filter_by(id=id).first()
    todolist.name = request.form.get('listname')
    db.session.commit()
    return redirect(url_for('show_list', id=todolist.id))

## Delete todolist
@app.route('/todolist/<int:id>/delete')
@login_required
def delete_list(id):
    todolist = ToDoList.query.filter_by(id=id).first()
    for activity in todolist.activities:
        db.session.delete(activity)
        db.session.commit()
    db.session.delete(todolist)
    db.session.commit()
    return redirect(url_for('home'))

# CRUD Activities
## Add new activity
@app.route('/todolist/<int:id>/activity/add', methods=['POST'])
@login_required
def add_activity(id):
    todolist = ToDoList.query.filter_by(id=id).first()
    new_activity = Activity(
        name= request.form.get('activity'),
        star=False,
        parent_list = todolist
    )
    db.session.add(new_activity)
    db.session.commit()
    return redirect(url_for('show_list', id=todolist.id))

## Update Activity
# TODO:
### Star Activity
### Color Activity
@app.route('/todolist/<int:list_id>/activity/<int:activity_id>/update', methods=['POST'])
@login_required
def update_activity(list_id, activity_id):
    todolist = ToDoList.query.filter_by(id=list_id).first()
    activity = Activity.query.filter_by(id=activity_id).first()
    activity.name = request.form.get('activity')
    db.session.commit()
    return redirect(url_for('show_list', id=todolist.id))

## Delete Activity
@app.route('/todolist/<int:list_id>/activity/<int:activity_id>/delete')
@login_required
def delete_activity(list_id, activity_id):
    todolist = ToDoList.query.filter_by(id=list_id).first()
    activity = Activity.query.filter_by(id=activity_id).first()
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('show_list', id=todolist.id))

# User Authentication
## Login
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        name = request.form.get("username")
        find_user = User.query.filter_by(username=name).first()
        if find_user == None:
            flash("You need to register an account first!") 
            return redirect(url_for('register'))
        elif check_password_hash(find_user.password, request.form.get('password')):
            login_user(find_user)
            return redirect(url_for('home'))
        else:
            flash('Wrong username or password!')
    return render_template('auth.html', form = form, purpose='login')

## Register
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method=='POST' and form.validate_on_submit():
        name = request.form.get("username")
        find_user = User.query.filter_by(username=name).first()
        if find_user == None:
            new_user = User(
                username=name, 
                password=generate_password_hash(
                    request.form.get('password'),
                    method='pbkdf2:sha256',
                    salt_length=13,
                )
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            flash("Account already exists!")
            return redirect(url_for('login'))
    return render_template('auth.html', form=form, purpose='register')

## Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)