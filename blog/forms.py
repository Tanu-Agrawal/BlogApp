from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),Length(min=2, max=20)])
    email    = StringField('Email',
                          validators=[DataRequired(),Email()])
    password  = PasswordField('Password' , validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #custom-Validation: to show error if username already exists while registering a new user

    # def validate_field(self,field):
    #     if True:
    #         raise ValidationError('validation message')

    def validate_username(self,username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username already exists!!')

    def validate_email(self,email):

        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('Email already registered!!')

class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),Length(min=2, max=20)])
    email    = StringField('Email',
                          validators=[DataRequired(),Email()])
    password  = PasswordField('Password' , validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content' , validators=[DataRequired()])
    submit = SubmitField('Post')
