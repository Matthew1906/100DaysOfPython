# Import Modules
from flask import Flask, render_template, request
import requests, smtplib

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

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=USER_MAIL, password=PASSWORD)
        #     connection.sendmail(
        #         from_addr=USER_MAIL, 
        #         to_addrs=TARGET_MAIL, 
        #         msg=f"Subject: New Contact\n\n"\
        #         f"Name: {request.form['name']}\n"\
        #         f"Email: {request.form['email']}\n"\
        #         f"Phone: {request.form['phone']}\n"\
        #         f"Message: {request.form['message']}\n"
        #     )
        pass
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
