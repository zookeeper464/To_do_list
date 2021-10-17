from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# 회원가입시 필요한 데이터 처리에 대한 클래스 설정
class ReigistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

# 로그인시 필요한 데이터 처리에 대한 클래스 설정
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
