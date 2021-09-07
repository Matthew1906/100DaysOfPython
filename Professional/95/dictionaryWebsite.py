# Web Development Functions
from flask import Flask, render_template, request, flash
from forms import WordSearchForm
# HTTP Requests Functions
from requests import get
# Utility Functions
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

dictionary_token = getenv('DICTIONARY_KEY')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = WordSearchForm()
    if request.method=='POST' and form.validate_on_submit():
        keyword = request.form.get('keyword')
        dictionary_url = f'https://owlbot.info/api/v4/dictionary/{keyword}'
        dictionary_header = {
            'Authorization':f'Token {dictionary_token}',
            'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = get(url=dictionary_url, headers=dictionary_header)
        if response.status_code == 200:
            return render_template('result.html', result=response.json())
        else:
            flash('Definition not found!')        
    return render_template('index.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)