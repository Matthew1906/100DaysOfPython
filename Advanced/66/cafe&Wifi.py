# Import modules
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}

db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route('/random')
def random_stuff():
    cafes = db.session.query(Cafe).all()
    cafe = choice(cafes)
    return jsonify(
        id = cafe.id,
        name = cafe.name,
        map_url = cafe.map_url,
        img_url = cafe.img_url,
        location = cafe.location,
        seats = cafe.seats,
        has_toilet = cafe.has_toilet,
        has_wifi = cafe.has_wifi,
        has_sockets = cafe.has_sockets,
        can_take_calls = cafe.can_take_calls,
        coffee_price = cafe.coffee_price,
    )

@app.route('/all')
def all_cafe():
    cafes = db.session.query(Cafe).all() 
    return jsonify(cafes = {cafe.name : cafe.to_dict() for cafe in cafes})

@app.route('/search')
def find_cafe():
    loc = request.args.get("loc")
    search_cafe = db.session.query(Cafe).filter(Cafe.location==loc)
    if search_cafe.first() is None:
        return jsonify(
            error = {
                'Not Found':"Sorry, we can't find a cafe at this location"
            }
        )
    return jsonify(results = {cafe.name : cafe.to_dict() for cafe in search_cafe})

## HTTP POST - Create Record
def true_or_false(string):
    if string=='true' or string =='True':
        return True
    else:
        return False


@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = true_or_false(request.form.get('has_toilet')),
        has_wifi = true_or_false(request.form.get('has_wifi')),
        has_sockets = true_or_false(request.form.get('has_sockets')),
        can_take_calls = true_or_false(request.form.get('can_take_calls')),
        coffee_price = request.form.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response = {
           'Success':"Successfully added new cafe"
        }
    )

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    to_update = db.session.query(Cafe).get(cafe_id)
    if to_update == None:
        return jsonify({
            "Error": f"Sorry, we can't find the cafe with id {cafe_id}"
        })
    to_update.coffee_price = request.args.get('coffee_price')
    db.session.commit()
    return jsonify({
        "Success":"Successfully updated the price!"
    })

## HTTP DELETE - Delete Record

MOCK_API_KEY = 'mock_api_key'
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    to_delete = db.session.query(Cafe).get(cafe_id)
    if to_delete == None:
        return jsonify({
            "Error": f"Sorry, we can't find the cafe with id {cafe_id}"
        })
    elif request.args.get('api_key') != MOCK_API_KEY:
        return jsonify({
            "Error": "You don't have permission!"
        })
    db.session.delete(to_delete)
    db.session.commit()
    return jsonify({
        "Success":"Successfully deleted the cafe!"
    })

# Driver Code
if __name__ == '__main__':
    app.run(debug=True)
