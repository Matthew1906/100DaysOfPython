# Import Modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from forms import CafeForm, LoginForm, ReviewForm
from csv import reader, writer

# Load Environment variables
load_dotenv()

# Constants
ADMIN_USERNAME = getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = generate_password_hash(getenv('PASSWORD'), method='pbkdf2:sha256', salt_length=13)
ADMIN_NAME = getenv('NAME')

# Create App
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
Bootstrap(app)

# Connect to Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Config Database
if getenv('DATABASE_URL') == None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe_wifi.db'
else: 
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL').replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Config Tables
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class Cafe(db.Model):
    __tablename__ = 'cafes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    image_url = db.Column(db.String(600), nullable=False)
    location = db.Column(db.String(255),  nullable=False)
    open_time = db.Column(db.String(255), nullable=False)
    close_time = db.Column(db.String(255), nullable=False)
    coffee_rating = db.Column(db.String(255), nullable=False)
    wifi_rating = db.Column(db.String(255), nullable=False)
    power_rating = db.Column(db.String(255), nullable=False)
    reviews = relationship("Review", back_populates='parent_cafe')
    
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(5000), nullable=False)
    cafe_id = db.Column(db.Integer, db.ForeignKey('cafes.id'))
    parent_cafe = relationship("Cafe", back_populates='reviews')

db.create_all()
admin = User(name='Matthew Adrianus Mulyono')
db.session.add(admin)
db.session.commit()
with open('cafe-data.csv', encoding='utf-8') as csv_file:
    csv_data = list(reader(csv_file, delimiter=','))
    for row in csv_data[1:]:
        # print(row)
        new_cafe = Cafe(
            name= row[0],
            image_url = row[1],
            location= row[2],
            open_time= row[3],
            close_time= row[4],
            coffee_rating= row[5],
            wifi_rating= row[6],
            power_rating= row[7],
        )
        db.session.add(new_cafe)
        db.session.commit()

# Default loading user function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Homepage Route
@app.route("/")
def home():
    return render_template("index.html")

# Add new Cafe 
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name = request.form.get('name'),
            image_url = request.form.get('image_url'),
            location = request.form.get('location'),
            open_time = request.form.get('open_time'),
            close_time = request.form.get('close_time'),
            coffee_rating = request.form.get('coffee_rating'),
            wifi_rating = request.form.get('wifi_rating'),
            power_rating = request.form.get('power_rating'),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

# Show all cafe route
@app.route('/cafes')
def cafes():
    cafes = Cafe.query.all()
    return render_template('cafes.html', cafes=cafes)

# Add a review
@app.route('/review/<int:id>', methods=['GET', 'POST'])
def review(id:int):
    form = ReviewForm()
    cafe = Cafe.query.filter_by(id=id).first()
    if request.method=='POST' and form.validate_on_submit():
        new_review = Review(
            name=request.form.get('name'),
            body=request.form.get('review'),
            parent_cafe = cafe
        )
        db.session.add(new_review)
        db.session.commit()
    return render_template('review.html', form=form, cafe=cafe)

# Admin Authentication
## Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        admin = User.query.filter_by(name=ADMIN_NAME).first()
        username = request.form.get('username')
        password = request.form.get('password')
        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD, password):
            login_user(admin)
            return redirect(url_for('cafes')) 
        flash('Wrong Username or Password!')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Driver Code
if __name__ == '__main__':
    app.run(debug=True)