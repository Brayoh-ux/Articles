from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import TextAreaField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length ,Required, ValidationError, Email, EqualTo
from app.models import User
from flask_login import current_user



class LoginForm(FlaskForm):
    email = StringField('Your Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Create Username', validators=[Required(), Length(min= 4, max=50)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Ooop! Someone took this username!!')

    def validate_email(self, email):
        
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Please use a different email address.')


class UpdateForm(FlaskForm):
    username = StringField('Create Username', validators=[Required(), Length(min= 4, max=50)])
    email = StringField('Email', validators=[Required(), Email()])
    picture = FileField('Update profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ooops! someone took this username!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user :
            raise ValidationError('Please use a different email address.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Post')