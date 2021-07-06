from flask import Flask, render_template
import random, datetime as dt, requests 

app = Flask(__name__)

# Jinja = templating language
@app.route('/')
def home():
    random_number = random.randint(1,3)
    return render_template("index.html", random_number = random_number, year = dt.datetime.now().year)

@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get('https://api.genderize.io', params = {'name':name}).json()['gender']
    age_response = requests.get('https://api.agify.io', params = {'name':name}).json()['age']
    return render_template("guess.html", name = name ,gender = gender_response, age = age_response)

@app.route('/blog/<num>')
def blog(num):
    blogs = requests.get('https://api.npoint.io/7bce33b15a477a7a6c81').json()
    return render_template("blog.html", blogs = blogs, idx = int(num))

if __name__ == '__main__':
    app.run(debug=True)