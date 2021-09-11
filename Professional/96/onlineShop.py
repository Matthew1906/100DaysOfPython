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
from functools import wraps
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import locale
# For initializing dataframe
import pandas as pd

# PROGRESS:
# - Flow of Program: Flowchart, ERD
# - Database: All done
# - Frontend: Header. Footer, show all products, individual products, product form, unfinished slider (need to add image)
# - Forms: Product, Login, Register
# - Authorizations: All done
# - Product Management: Add Product, Update Product
# - Admin Access: Decorator is done, condition on product management
# - Cart Function
# - Product Review
# - Search Function
# - Pagination
# - Checkout and Payment Processing

# Load Environment Variables
load_dotenv()

# Configure Locale
locale.setlocale(locale.LC_ALL, 'IND')

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

# Setup Decorator
def admin_only(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1 :
            return func(*args, **kwargs)
        return abort(403)
    return decorated_function

# Setup Template filter
@app.template_filter('format_currency')
def format_currency(price:int):
    return locale.currency(float(price))

@app.template_filter('refactor_categories')
def refactor_categories(categories:list):
    if len(categories) == 0:
        return 'Miscellaneous'
    return ', '.join([pc.category.name.replace('And', ' & ') for pc in categories])

# Main route
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products = products)

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
@app.route('/products/add', methods=['GET','POST'])
@admin_only
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        find_product = Product.query.filter_by(name=request.form.get('name')).first()
        if find_product is None:
            new_product = Product(
                name = request.form.get('name'),
                description = request.form.get('description'),
                image_url = request.form.get('image_url'),
                price = request.form.get('price'),
                stock = request.form.get('stock'),
            )
            with app.app_context():
                db.session.add(new_product)
                db.session.commit()
                for category in form.categories.data:
                    new_product_category = ProductCategory(
                        product = new_product,
                        category = Category.query.filter_by(name=category).first()
                    )
                db.session.add(new_product_category)
                db.session.commit()
            return redirect(url_for('home'))
    return render_template('product_manager.html', purpose = 'add', form = form)

@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
@admin_only
def update_product(id:int):
    product = Product.query.filter_by(id=id).first()
    form = ProductForm(
        name = product.name,
        description=product.description,
        image_url=product.image_url,
        price = product.price,
        stock = product.stock,
        categories = [category for category in product.categories]
    )
    if form.validate_on_submit():
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.image_url = request.form.get('image_url')
        product.price = request.form.get('price')
        product.stock = request.form.get('stock')
        categories = ProductCategory.query.filter_by(product_id=id)
        with app.app_context():
            for category in categories:
                db.session.delete(category)
                db.session.commit()
            for category in form.categories.data:
                new_product_category = ProductCategory(
                    product = product,
                    category = Category.query.filter_by(name=category).first()
                )
                db.session.add(new_product_category)
                db.session.commit()
        return redirect(url_for('get_product', id=id))
    return render_template('product_manager.html', product=product, purpose = 'update', form = form)

# Add to Cart
@app.route('/products/<int:id>', methods=['GET','POST'])
def get_product(id:int):
    product = Product.query.filter_by(id=id).first()
    return render_template('product_manager.html', product=product, purpose = 'get')

# Checkout


# Transaction History

# Driver code
if __name__ == '__main__':
    app.run(debug=True)