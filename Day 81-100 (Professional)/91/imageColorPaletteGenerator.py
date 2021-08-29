# Day 91 of 100 Days of Python
# Project Name: Image Colour Palette Generator
# Things I implements: Web Development with Flask, Image Processing with Pillow, Numpy, and Matplotlib 

# Import modules
## Flask -> Generate the Website
from flask import Flask, render_template, request, url_for, flash, abort, redirect
## Forms -> Image forms + form validation
from forms import ImageForm
## Image handling and encoding-> using PIL, collections, numpy, matplotlib, and Base64
from color_finder import get_image, find_top_colors, reshape_colors
from base64 import b64encode
## Get Environment Variables
from dotenv import load_dotenv
from os import getenv
## Utilities
from pyperclip import copy
from functools import wraps

# Load Environment variables
load_dotenv()

# Configure Application
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# Use global variables to store necessary variables
image_uri, top_colors = None, None

# Decorator to ensure that the variables are not None
def isNaN(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        global image_uri, top_colors
        if image_uri is not None and top_colors is not None:
            return func(*args, **kwargs)
        return abort(403)
    return decorated_function

# Configure routes
@app.route('/', methods=['GET', 'POST'])
def home():
    global image_uri, top_colors
    form = ImageForm()
    if request.method=='POST':
        if form.validate_on_submit():
            # Store in file for later uses
            image_file = request.files.get('image')
            # Create URI for the image file
            ## How to render image without saving: https://stackoverflow.com/questions/24219446/render-image-without-saving
            encoded = b64encode(image_file.read()).decode('utf-8')
            mime = "image/jpeg"
            image_uri = f"data:{mime};base64,{encoded}"
            # Get colors
            ## Get the ndarray from image file
            image_array = get_image(image_file)
            ## Retrieve the top 10 colors
            top_colors = find_top_colors(image_array)
            ## Reshape the top 10 colors into dictionary of hexcodes
            top_colors = reshape_colors(top_colors)
            return redirect(url_for('result', image=image_uri, colors=top_colors))
        else:
            flash('Invalid input, please make sure that the image is in jpg/png!')
    return render_template('index.html', form=form)

@app.route('/result')
@isNaN
def result():
    '''Show the analysis result'''
    return render_template('result.html', image=image_uri, colors = top_colors)

@app.route('/copy_color/<hex_code>')
@isNaN
def copy_hexcode(hex_code:str):
    '''Copy the hexcode of the selected color into clipboard'''
    copy(hex_code)
    return redirect(url_for('result', image=image_uri, colors=top_colors))

if __name__ == '__main__':
    app.run(debug=True)