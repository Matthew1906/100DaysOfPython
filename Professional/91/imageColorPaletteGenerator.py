# Import modules
## Flask -> Generate the Website
from flask import Flask, render_template, request, url_for, flash, abort, redirect
## Forms -> Image forms + form validation
from forms import ImageForm
## Image handling and encoding-> using PIL, collections, numpy, matplotlib, and Base64
from color_finder import get_image, get_length, find_top_colors, reshape_colors
from base64 import b64encode
## Get Environment Variables
from dotenv import load_dotenv
from os import getenv

# Load Environment variables
load_dotenv()

# Configure Application
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# Configure routes
@app.route('/', methods=['GET', 'POST'])
def home():
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
            image_length = get_length(image_array)
            ## Retrieve the top 10 colors
            top_colors = find_top_colors(image_array)
            if top_colors is False:
                flash('Invalid input!')
                return render_template('index.html', form=form)
            ## Reshape the top 10 colors into dictionary of hexcodes
            top_colors = reshape_colors(top_colors, image_length)
            return render_template('result.html', image=image_uri, colors=top_colors)
        else:
            flash('Invalid input, please make sure that the image is in jpg/png!')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)