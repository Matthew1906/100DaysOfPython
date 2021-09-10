# Web Development
from flask import Flask, render_template, request, redirect, url_for, flash
# Login Manager
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
# Forms
from forms import LoginForm, RegisterForm, ProductForm
# Database
from models import db, User, Product, ProductReview, Order, Transaction, TransactionDetail, Category, ProductCategory
# Utilities
from datetime import datetime
from dotenv import load_dotenv
from os import getenv

# PROGRESS:
# - Flow of Program: Flowchart, ERD
# - Database: All done
# - Frontend: Header. Footer
# - Forms: Product, Login, Register
# - Authorizations
# - Admin Access
# - Cart Function
# - Checkout and Payment Processing

# Load Environment Variables
load_dotenv()

# Create App
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Config Database URL
if getenv('DATABASE_URL') == None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online-shop.db'
else: 
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL').replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db.init_app(app)
# Paste code from init.txt here

# Default loading user function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template('index.html')

# User Authentication
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        find_user = User.query.filter_by(email=request.form.get('email')).first()
        if find_user is None:
            new_user = User(
                name = request.form.get('name'),
                email = request.form.get('email'),
                password = generate_password_hash(
                    request.form.get('password'),
                    method='pbkdf2:sha256',
                    salt_length=13,
                ),
                dob = datetime.strptime(request.form.get('dob'),'%Y-%m-%d'),
            )
            with app.app_context():
                db.session.add(new_user)
                db.session.commit()
        else:
            flash('User already exists, Please login!')
        return redirect(url_for('login'))
    return render_template('auth.html', form=form, purpose='register')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Login")
        find_user = User.query.filter_by(email=request.form.get('email')).first()
        if find_user is None:
            flash("User doesn't exist! Please register!")
            return redirect(url_for('register'))
        elif check_password_hash(find_user.password, request.form.get('password')):
            login_user(find_user)
            return redirect(url_for('home'))
        else:
            flash('Wrong email or password!')
    return render_template('auth.html', form=form, purpose='login')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Product Management -> Admin Access


# Add to Cart


# Checkout


# Transaction History

# Driver code
if __name__ == '__main__':
    app.run(debug=True)