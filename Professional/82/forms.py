from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, PasswordField, StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, regexp, URL

class ProjectForm(FlaskForm):
    name = StringField("Project name", validators=[DataRequired()])
    type = SelectField("Type", choices=[('Scripting', 'Scripting'), ('GUI (Tkinter or Turtle)', 'GUI'), ('HTTP Requests & APIs', 'HTTP Requests and APIs'), ('Automation', 'Automation'), ('Web Development', 'Web Development'), ('Data Science','Data Science')],validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    link = StringField('Link', validators=[URL()])
    image1 = FileField("Image 1", validators=[DataRequired(), FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    cap1 = StringField("Image 1 Caption", validators=[DataRequired()])
    desc1 = StringField("Image 1 Description", validators=[DataRequired()])
    image2 = FileField("Image 2", validators=[DataRequired(), FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    cap2 = StringField("Image 2 Caption", validators=[DataRequired()])
    desc2 = StringField("Image 2 Description", validators=[DataRequired()])
    image3 = FileField("Image 3", validators=[DataRequired(), FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    cap3 = StringField("Image 3 Caption", validators=[DataRequired()])
    desc3 = StringField("Image 3 Description", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')
