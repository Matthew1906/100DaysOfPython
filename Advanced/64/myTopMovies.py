# Import Modules
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

# Create App
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-10-movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

# Setup Database
movie_db = SQLAlchemy(app)

class Movie(movie_db.Model):
    movie_id = movie_db.Column(movie_db.Integer, primary_key=True)
    title = movie_db.Column(movie_db.String(255), unique=True, nullable=False)
    year = movie_db.Column(movie_db.Integer, nullable=False)
    description = movie_db.Column(movie_db.String(5000), nullable=False)
    rating = movie_db.Column(movie_db.Float, nullable=False)
    ranking = movie_db.Column(movie_db.Integer, nullable=False)
    review = movie_db.Column(movie_db.String(5000), nullable=False)
    img_url = movie_db.Column(movie_db.String(5000), nullable=False)

movie_db.create_all()

# When running the program for the first time, it is necessary to uncomment the code below, else, comment them
# first_movie = Movie(
#     title = 'V for Vendetta',
#     year = 2005,
#     description = 'In a future British tyranny, a shadowy freedom fighter, known only by the alias of "V", plots to overthrow it with the help of a young woman.',
#     rating = 8.1,
#     ranking = 10,
#     review = 'Utterly Spectacular!',
#     img_url = 'https://upload.wikimedia.org/wikipedia/id/9/9f/Vforvendettamov.jpg'
# )

# movie_db.session.add(first_movie)
# movie_db.session.commit()

# Home -> display all movies
@app.route("/")
def home():
    movies = movie_db.session.query(Movie).order_by(Movie.rating.desc())
    rank = 1
    for movie in movies:
        movie.ranking = rank
        rank+=1
        movie_db.session.commit()
    return render_template("index.html", movies=movies)

# Edit Movie Rating and Review
class EditForm(FlaskForm):
    rating = FloatField(validators=[DataRequired()])
    review = StringField(validators=[DataRequired()])
    submit = SubmitField("Done")

@app.route("/edit/<movie_id>", methods=['GET','POST'])
def edit(movie_id):
    to_edit= Movie.query.get(movie_id)
    if request.method=='POST':
        to_edit.rating = request.form['rating']
        to_edit.review = request.form['review']
        movie_db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=to_edit, form=EditForm())

# Delete Movie
@app.route('/delete/<movie_id>')
def delete(movie_id):
    to_delete = Movie.query.get(movie_id)
    movie_db.session.delete(to_delete)
    movie_db.session.commit()
    return redirect(url_for('home'))

# Add Movie
class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    search = SubmitField("Find Movie")

@app.route('/add')
def add():
    return render_template('add.html', form = AddForm())

# Search Movies
@app.route('/search', methods=['POST','GET'])
def select():
    search_url ='https://api.themoviedb.org/3/search/movie'
    search_params = {
        'api_key' : 'a28e4cc0d1976709b32c0900d73dda0e',
        'query' : request.form['title']
    }
    search_responses = requests.get(url=search_url, params=search_params).json()['results']
    search_results = [
        Movie(
            movie_id = search_response['id'],
            title = search_response['original_title'],
            year = search_response['release_date'][:4],
            description = search_response['overview'],
            ranking = 1,
            rating = search_response['vote_average'],
            review = 'No Review',
            img_url= f'https://image.tmdb.org/t/p/w500/{search_response["poster_path"]}'
        ) for search_response in search_responses
    ]
    return render_template('select.html', results=search_results)

# Save the Movies
@app.route('/save/<movie_id>')
def save(movie_id):
    save_url = 'https://api.themoviedb.org/3/movie/' + movie_id
    save_params = {'api_key' : 'a28e4cc0d1976709b32c0900d73dda0e'}
    save_response = requests.get(url=save_url, params=save_params).json()
    new_movie = Movie(
        movie_id = save_response['id'],
        title = save_response['original_title'],
        year = save_response['release_date'][:4],
        description = save_response['overview'],
        ranking = 1,
        rating = save_response['vote_average'],
        review = 'No Review',
        img_url= 'https://image.tmdb.org/t/p/w500/'+ save_response['poster_path']
    )
    movie_db.session.add(new_movie)
    movie_db.session.commit()
    return redirect(url_for('edit', movie_id = new_movie.movie_id))

# Driver Code
if __name__ == '__main__':
    app.run(debug=True)