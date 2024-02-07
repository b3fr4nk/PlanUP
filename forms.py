from flask_wtf import FlaskForm
import re
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField, ValidationError, IntegerField, FileField
from wtforms.validators import DataRequired, Length, NumberRange
from models import User
from extensions import bcrypt


def length(min=1, max=1000):
    message = f'Must be between {min} and {max} characters long.'

    def _length(form, field):
        l = len(field.data)
        if l < min or max != -1 and l > max:
            raise ValidationError(message)

    return _length


class ValidatePassword(object):
    def __init__(self, min=8, max=100) -> None:
        self.min = min
        self.max = max
        self.message = ['Password must contain at least one symbol, one uppercase letter, one lowercase letter, and one number',
                        'Password must be between 6 and 100 characters long']

    def __call__(self, form, field):
        l = len(field.data)
        if l < self.min or self.max != -1 and l > self.max:
            match = re.findall(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", field.data)
            if len(match) < 1:
                raise ValidationError(self.message[0])
            raise ValidationError(self.message[1])


class PostForm(FlaskForm):
    """Form for creating a new post"""

    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    media = FileField('Media')


class SignupForm(FlaskForm):
    """Form for creating a new user"""

    username = StringField('Username', validators=[
                           DataRequired(), length(min=5, max=18)])
    password = PasswordField("Password", validators=[
                             DataRequired(), ValidatePassword()])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError(
                'No user with that username. Please try again.')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not bcrypt.check_password_hash(
                user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')
