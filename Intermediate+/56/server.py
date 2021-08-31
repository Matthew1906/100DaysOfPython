# Day 56 Project of 100 Days of Python
# Project Name: Static Personal Site using Template and Flask
# Things i implemented: Flask, Website Templates

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)