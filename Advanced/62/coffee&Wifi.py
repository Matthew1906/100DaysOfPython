# Import Modules
from flask import Flask, render_template, request 
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
from datetime import datetime
import csv

# Create App
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Choice template
rating = [('✘')]

# Cafe Form Class
class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
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

# Homepage Route
@app.route("/")
def home():
    return render_template("index.html")

# Add new Cafe Route
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = [form.name.data, form.location.data, form.open_time.data.strftime('%H:%M'), form.close_time.data.strftime('%H:%M'), form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
        with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
    return render_template('add.html', form=form)

# Show all cafes route
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

# Driver Code
if __name__ == '__main__':
    app.run(debug=True)
