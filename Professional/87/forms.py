# Import Modules
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL
from datetime import datetime

# Choice template
rating = [('✘')]

# Cafe Form Class
class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    image_url = StringField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = TimeField('Open Time (HH:MM)', format='%H:%M',validators = [DataRequired()])
    close_time = TimeField('Close Time (HH:MM)', format='%H:%M', validators = [DataRequired()])
    coffee_rating = SelectField(
        label='Coffee Rating', 
        validators=[DataRequired()],
        choices= rating + [('☕️'*i) for i in range(1,6)]
    )
    wifi_rating = SelectField(
        label='Wifi Rating', 
        validators=[DataRequired()],
        choices= rating + [('💪'*i) for i in range(1,6)]
    )
    power_rating = SelectField(
        label='Power Outlet Rating', 
        validators=[DataRequired()],
        choices= rating+ [('🔌'*i) for i in range(1,6)]
    )
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class ReviewForm(FlaskForm):
    name = StringField(label='Username', validators=[DataRequired()])
    review = TextAreaField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
