# Import modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Setup Database

# A. The sqlite3 method
# library = sqlite3.connect('all_books.db')
# library_cursor = library.cursor()
# library_cursor.execute('CREATE TABLE books(id INTEGER PRIMARY KEY,title varchar(255) NOT NULL UNIQUE,author varchar(55) NOT NULL,rating float NOT NULL)')

# B. The sqlalchemy method

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255), unique=True, nullable=False)
    book_author = db.Column(db.String(55), nullable=False)
    book_rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return '<Book %r>' % self.book_title

db.create_all()

# The routes
@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books= all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method=='POST':
        new_book = Book(book_title = request.form['title'],
            book_author = request.form['author'],
            book_rating = request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_rating(id):
    to_edit = Book.query.get(id)
    if request.method == 'POST':
        to_edit.book_rating = request.form['newrating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=to_edit)

@app.route('/delete/<id>')
def delete(id):
    to_delete = Book.query.get(id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# Driver code
if __name__ == "__main__":
    app.run(debug=True)
