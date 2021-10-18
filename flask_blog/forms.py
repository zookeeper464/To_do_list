from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

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

# 로그인시 필요한 데이터 처리에 대한 클래스 설정
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
