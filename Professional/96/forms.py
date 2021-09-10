from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField , PasswordField, SubmitField, IntegerField, SelectMultipleField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, URL, email

# Authentication
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    dob = DateField('Date of Birth', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField("Login")

# Product
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[InputRequired()])
    description = TextAreaField('Product Description', validators=[InputRequired()])
    image_url = StringField('Product Image URL', validators=[InputRequired(), URL()])
    price = IntegerField('Product Price', validators=[InputRequired()])
    stock = IntegerField('Stock', validators=[InputRequired()])
    categories = SelectMultipleField(
        label='Categories', 
        choices=[
            ('Automotive', 'Automotive'), ('ArtsAndCrafts','Arts and Crafts'),
            ('Books', 'Books'), ('Clothing','Clothing'), 
            ('Electronics', 'Electronics'), ('Food', 'Food and Beverages'),
            ('HealthAndBeauty','Health and Beauty'),('HomeAndGarden', 'Home and Garden'), 
            ('Office', 'Office'), ('SportsAndOutdoor','Sports & Outdoor Activities')
        ],
        validators=[InputRequired()]
    )