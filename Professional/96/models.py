# Database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship 
from flask_login import UserMixin

db = SQLAlchemy()

# Config tables
class User(db.Model, UserMixin):
    '''User Table'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    cart = relationship('Order', back_populates='user')
    reviews = relationship('ProductReview', back_populates='user')
    transactions = relationship('Transaction', back_populates='user')

class Product(db.Model):
    '''Product Table'''
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    image_url = db.Column(db.String(5000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    orders = relationship('Order', back_populates='product')
    reviews = relationship('ProductReview', back_populates='product')   
    transaction_details = relationship('TransactionDetail', back_populates='product')
    categories = relationship('ProductCategory', back_populates='product')

class Order(db.Model):
    '''Cart containing Products'''
    __tablename__ = 'orders'
    user = relationship('User', back_populates='cart')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    product = relationship('Product', back_populates='orders')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

class ProductReview(db.Model):
    '''Product Review Table'''
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user = relationship('User', back_populates='reviews')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product = relationship('Product', back_populates='reviews')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(5000), nullable=False)

class Transaction(db.Model):
    '''Transaction table'''
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user = relationship('User', back_populates='transactions')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    details = relationship('TransactionDetail', back_populates='transaction')
    payment_method = db.Column(db.String(255), nullable=False)
    payment_status = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(5000), nullable=False)
    delivery_cost = db.Column(db.Integer, nullable=False)
    delivery_status = db.Column(db.String(255), nullable=False)
    
class TransactionDetail(db.Model):
    '''Details regarding transaction'''
    __tablename__ = 'transaction_details'
    transaction = relationship('Transaction', back_populates='details')
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), primary_key=True)
    product = relationship('Product', back_populates='transaction_details')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Category(db.Model):
    '''Category table'''
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    product_categories = relationship('ProductCategory', back_populates ='category')

class ProductCategory(db.Model):
    '''Product categories'''
    __tablename__ = 'product_categories'
    product = relationship('Product', back_populates='categories')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    category = relationship('Category', back_populates='product_categories')
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)
