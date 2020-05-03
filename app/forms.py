from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-enter Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if len(username.data) > 64:
            raise ValidationError('Username Cannot be longer than 64 characters.')

        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already taken. please choose a different value.')

    def validate_email(self, email):
        if len(email.data) > 120:
            raise ValidationError('Email Cannot be longer than 120 characters.')

        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('An account with that email already exists. You can sign in via the Login Page.')

    def validate_password(self, password):
        if len(password.data) < 8:
            raise ValidationError('Password must be at least 8 characters long.')

