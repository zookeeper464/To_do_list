from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from .models import User

# 회원가입시 필요한 데이터 처리에 대한 클래스 설정
class ReigistrationForm(FlaskForm): # DataRequired를 통해 변수 입력
    # 
    username = StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
                        # Email을 통해 이메일 여부 확인

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
                        # EqualTo를 통해 비밀번호 일치 여부확인

    submit = SubmitField('Sign Up') # 제출시 필요한 변수, 포스트 할때 302로 호출받는다.

    def validate_username(self,username): # 실행시 가져올 수 있는 변수명에 대한 내용을 함수명에 넣어야 한다.
        user = User.query.filter_by(username=username.data).first() # orm
        if user:
            raise ValidationError('That username is taken. Please choose a differnt one.') # 특정 상황에서 에러와 에러 문구를 띄우는 함수

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a differnt one.')

# 로그인시 필요한 데이터 처리에 대한 클래스 설정
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# account 데이터 변경을 위한 데이터 처리에 대한 클래스
class UpdateAccountForm(FlaskForm): # DataRequired를 통해 변수 입력
    username = StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])

    submit = SubmitField('Update') # 제출시 필요한 변수, 포스트 할때 302로 호출받는다.

    def validate_username(self,username): # 실행시 가져올 수 있는 변수명에 대한 내용을 함수명에 넣어야 한다.
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first() # orm

            if user:
                raise ValidationError('That username is taken. Please choose a differnt one.') # 특정 상황에서 에러와 에러 문구를 띄우는 함수

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a differnt one.')