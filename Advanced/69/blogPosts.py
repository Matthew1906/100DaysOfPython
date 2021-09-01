# Import Modules
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm, ContactForm
from flask_gravatar import Gravatar
from functools import wraps
import smtplib, os

# Constants
USER_MAIL = os.getenv("USER_MAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")
TARGET_MAIL = os.getenv("TARGET_MAIL")

# Configure Application
app = Flask(__name__)
if os.getenv('SECRET_KEY') == None:
    app.config['SECRET_KEY'] = '6k&A7$(16ENJ&%(E6xU8'
else:
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app,size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)

# Connect to Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Connect to database
if os.getenv('DATABASE_URL') == None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
else: 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace("postgres", "postgresql")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Configure tables 
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comments", back_populates = "author")
    
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = relationship("User", back_populates='posts')
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comments", back_populates ="parent_post")

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author = relationship("User", back_populates='comments')
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    parent_post = relationship("BlogPost", back_populates="comments")
    body = db.Column(db.Text, nullable = False)

# Default loading user function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Decorator for Admin privileges
def admin_only(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1 :
            return func(*args, **kwargs)
        return abort(403)
    return decorated_function

# Routes 
## Homepage
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)

## Register Account
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method=='POST' and form.validate_on_submit():
        check_user = User.query.filter_by(email=request.form.get('email')).first()
        if check_user!= None:
            flash("User already exists, Log in with this email!")
            return redirect(url_for('login'))
        new_user = User(
            email=request.form.get('email'), 
            password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=13),
            name= request.form.get('name'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form = form)

## Login Account
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        find_user = User.query.filter_by(email=request.form.get('email')).first()
        if find_user == None:
            flash("Please Register first!")
            return redirect(url_for('register'))
        elif check_password_hash(find_user.password, request.form.get('password')):
            login_user(find_user)
            return redirect(url_for('get_all_posts'))
        else:
            flash("Wrong Password!")
            return redirect(url_for('login'))
    return render_template("login.html", form = form)

## Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))

## Individual posts page
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    comment_form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    if request.method == 'POST' and comment_form.validate_on_submit():
        if not current_user.is_authenticated :
            flash("You need to login to comment!")
            return redirect(url_for('login'))
        new_comment = Comments(
            author = current_user,
            parent_post = requested_post,
            body = request.form.get("body"),
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, form = comment_form)

## About Me Page
@app.route("/about")
def about():
    return render_template("about.html")

## Contact Me Page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if request.method == 'POST':
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER_MAIL, password=USER_PASSWORD)
            connection.sendmail(
                from_addr=USER_MAIL, 
                to_addrs=TARGET_MAIL, 
                msg=f"Subject: New Contact\n\n"\
                f"Name: {request.form['name']}\n"\
                f"Email: {request.form['email']}\n"\
                f"Phone: {request.form['phone']}\n"\
                f"Message: {request.form['message']}\n"
            )
        return redirect(url_for('get_all_posts'))
    return render_template("contact.html", form = contact_form)

## Make new post - Admin Privilege
@app.route("/new-post", methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if request.method=='POST' and form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

## Edit post - Admin Privilege
@app.route("/edit-post/<int:post_id>", methods=['POST', 'GET'])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if request.method=='POST' and edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)

## Delete post - Admin Privilege
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Driver Code
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)