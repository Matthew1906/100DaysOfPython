# Day 59 of 100 Days of Python
# Project Name: Personal Blog (Part 2)
# Things i implemented: Flask, render templates, requests, kwargs
# This project will keep improving (so there might be copies of the same folders)

# Import Modules
from flask import Flask, render_template
import requests

# Initialize App
app = Flask(__name__)

# Create Class
class Post:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.author = kwargs['author']
        self.title = kwargs['title']
        self.subtitle = kwargs['subtitle']
        self.body = kwargs['body']
        self.date = kwargs['date']
        self.image = kwargs['image']

# Create List of Classes
post_responses = requests.get('https://api.npoint.io/e42b353ee387383898c7').json()
posts = [Post(**post_response) for post_response in post_responses]

# Set Up Routes
@app.route('/')
def index():
    return render_template('index.html', posts = posts)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts/<index>')
def post(index):
    return render_template('post.html', post=posts[int(index)-1])

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)