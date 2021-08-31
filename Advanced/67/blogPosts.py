# Day 67 Project of 100 Days of Python
# Project Name: Improved Blog Post (I call them Blog Post 3)
# Things i implemented: Flask, Wtforms, Bootstrap, SQLAlchemy, CKEditor, Datetime

# Import Modules
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt 

# Create App
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Table
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForms
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# App Routes
@app.route('/')
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).all()
    requested_post = None
    for blog_post in posts:
        print(blog_post.id)
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    add_form = CreatePostForm()
    if request.method == 'POST' and add_form.validate_on_submit():
        newPost = BlogPost(
            title = request.form['title'],
            subtitle = request.form['subtitle'],
            author = request.form['author'],
            body = request.form['body'],
            img_url = request.form['img_url'],
            date = dt.datetime.today().strftime('%B %d, %Y')
        )
        db.session.add(newPost)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('make-post.html', title = 'New Post', is_edit=False, form = add_form)

@app.route('/edit_post/<post_id>', methods=['GET','POST'])
def edit_post(post_id):
    to_edit = db.session.query(BlogPost).get(post_id)
    edit_form = CreatePostForm(
        title = to_edit.title,
        subtitle = to_edit.subtitle,
        author = to_edit.author,
        body = to_edit.body,
        img_url = to_edit.img_url,
    )
    if request.method == 'POST' and edit_form.validate_on_submit():
        to_edit.title = request.form['title']
        to_edit.subtitle = request.form['subtitle']
        to_edit.author = request.form['author']
        to_edit.body = request.form['body']
        to_edit.img_url =request.form['img_url']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('make-post.html', is_edit = True, title='Edit Post', form = edit_form, post_id=post_id)

@app.route('/delete/<post_id>')
def delete(post_id):
    to_delete = db.session.query(BlogPost).get(post_id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# Driver Code
if __name__ == "__main__":
    app.run(debug=True)