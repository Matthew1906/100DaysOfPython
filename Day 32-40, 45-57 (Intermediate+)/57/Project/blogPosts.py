# Day 57 of 100 Days of Python
# Project Name: Blog Posts
# Things i implemented: Flask and Requests

from flask import Flask, render_template
from post import Post
import requests 

app = Flask(__name__)

# Initialize Content
post_responses = requests.get('https://api.npoint.io/7bce33b15a477a7a6c81').json()
posts = []
for post_response in post_responses:
    print(post_response)
    posts.append(Post(post_response['id'], post_response['title'], post_response['subtitle'], post_response['body']))

@app.route('/')
def home():
    return render_template("index.html", posts = posts)

@app.route('/post/<index>')
def post(index):
    return render_template("post.html", post  = posts[int(index)-1])

if __name__ == "__main__":
    app.run(debug=True)
