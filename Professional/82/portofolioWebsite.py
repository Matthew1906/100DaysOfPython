# Day 82 of 100 Days of Python
# Project Name: Portofolio Website
# Things I implemented: Backend Web Development with Flask, Bootstrap, File processing

'''
TODO:
- project.html page -> show image
- deployment
'''

from flask import Flask, render_template, redirect, request , flash, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required, logout_user, login_user, LoginManager, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from forms import ProjectForm, LoginForm
from dotenv import load_dotenv
from base64 import b64encode, b64decode
from PIL import Image
from io import BytesIO #Converts data from Database into bytes
import os

# Load Environment variables
load_dotenv()

# Constants
ADMIN_NAME = os.getenv('ADMIN_NAME')
ADMIN_USERNAME = os.getenv('ADMIN')
ADMIN_PASSWORD = generate_password_hash(os.getenv('PASSWORD'), method='pbkdf2:sha256', salt_length=13)

# Config Application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap(app)

# Connect to Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Config Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portofolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255))
    description = db.Column(db.String(3000), nullable=False)
    image1 = db.Column(db.LargeBinary, nullable=False)
    cap1 = db.Column(db.String(255), nullable=False)
    desc1 = db.Column(db.String(255), nullable=False)
    image2 = db.Column(db.LargeBinary, nullable=False)
    cap2 = db.Column(db.String(255), nullable=False)
    desc2 = db.Column(db.String(255), nullable=False)
    image3 = db.Column(db.LargeBinary, nullable=False)
    cap3 = db.Column(db.String(255), nullable=False)
    desc3 = db.Column(db.String(255), nullable=False)

# This needs to be executed, and then commented
# db.create_all()
# admin = User(name=ADMIN_NAME)
# db.session.add(admin)
# db.session.commit()

# Default loading user function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# CRUD
## Read
@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects= projects)

@app.route('/<type>')
def by_type(type):
    projects = Project.query.filter_by(type=type)
    return render_template('index.html', projects= projects)

@app.route('/project/<int:id>')
def project(id):
    project = Project.query.get(id)
    images = []
    images.append(b64encode(project.image1).decode("utf-8"))
    images.append(b64encode(project.image2).decode("utf-8"))
    images.append(b64encode(project.image3).decode("utf-8"))
    return render_template('project.html', project = project, images=images)

## Create
@app.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
    form = ProjectForm()
    if request.method == 'POST':
        find_project = Project.query.filter_by(name=request.form.get('name')).first()
        if form.validate_on_submit() and find_project==None:
            new_project = Project(
                name = request.form.get('name'),
                type = request.form.get('type'),
                link = request.form.get('link'),
                description = request.form.get('description'),
                image1 = request.files.get('image1').read(),
                cap1 = request.form.get('cap1'),
                desc1= request.form.get('desc1'),
                image2 = request.files.get('image2').read(),
                cap2 = request.form.get('cap2'),
                desc2= request.form.get('desc2'),
                image3 = request.files.get('image3').read(),
                cap3 = request.form.get('cap3'),
                desc3= request.form.get('desc3'),
            )
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for('home'))
        else: 
            flash('Invalid Data!')
    return render_template('add.html', form = form)

## Update
@app.route('/update/<int:id>', methods=['POST', 'GET'])
@login_required
def update(id):
    project = Project.query.get(id)
    form = ProjectForm(
        name = project.name,
        type = project.type,
        link = project.link,
        description = project.description,
        image1 = project.image1,
        cap1 = project.cap1,
        desc1= project.desc1,
        image2 = project.image2,
        cap2 = project.cap2,
        desc2= project.desc2,
        image3 = project.image3,
        cap3 = project.cap3,
        desc3= project.desc3,
    )
    if request.method == 'POST' and form.validate_on_submit():
        project.name = request.form.get('name')
        project.type = request.form.get('type')
        project.link = request.form.get('link')
        project.description = request.form.get('description')
        project.image1 = request.files.get('image1').read()
        project.cap1 = request.form.get('cap1')
        project.desc1= request.form.get('desc1')
        project.image2 = request.files.get('image2').read()
        project.cap2 = request.form.get('cap2')
        project.desc2= request.form.get('desc2')
        project.image3 = request.files.get('image3').read()
        project.cap3 = request.form.get('cap3')
        project.desc3= request.form.get('desc3')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form = form, edit = True)

## Delete
@app.route('/delete/<id>')
@login_required
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('home'))

# User Admin Authentication
## Login
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        admin = User.query.filter_by(name=ADMIN_NAME).first()
        if request.form.get('username') == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD, request.form.get('password')):
            login_user(admin)
            return redirect(url_for('home'))
        flash('Wrong username or password!')
    return render_template('login.html', form = form)

## Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Extra feature -> about page
@app.route('/about')
def about():
    return render_template('about.html')
    
# Driver Code
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
