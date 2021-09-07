from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

class WordSearchForm(FlaskForm):
    keyword = StringField('Word to Search', validators=[DataRequired()])
    submit = SubmitField('Search')