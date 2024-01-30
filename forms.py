from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
from models import Post
from grocery_app.extensions import bcrypt

class PostForm(FlaskForm):
  """Form for creating a new post"""

  title = StringField('Title', validators=[DataRequired()])
  description = StringField('Description', validators=[DataRequired()])
  media = FileField('Media', )
  submit = SubmitField('Submit')