# Framework: An Architecture
# Library: Reusable Code

from flask import Flask

app = Flask(__name__)
print(__name__) #Special Attributes
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/bye')
def bye_world():
    return "<h1>Goodbye, Moon man </h1>"

if __name__== '__main__':
    app.run() # run the app faster than using the steps in course content