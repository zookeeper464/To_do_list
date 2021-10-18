from flask import render_template, url_for, flash, redirect
from flask_blog import app
from .forms import ReigistrationForm, LoginForm
from .models import User, Post
# reder_template는 flask에서 html을 호출하기 위한 모듈

posts = [
    {
        'author' : 'zookeeper_464',
        'title' : 'to_do_list',
        'content' : 'to make flask_to_do_list',
        'date_posted' : '2021-10-15'
    },
    
    {
        'author' : 'zookeeper_464',
        'title' : 'to_do_list(1)',
        'content' : 'to make flask_to_do_list second',
        'date_posted' : '2021-10-16'
    }
]

@app.route('/') # 기본인덱스에 대한 설정
@app.route('/home') # route는 여러개 설정해도 좋다.
def home():
    return render_template('home.html', posts=posts)
    # posts는 python에서 html로 보내는 변수를 의미한다.
    # posts가 아닌 다른 변수명을 활용하여 html에서 받아도 상관없다.

@app.route('/about') # 새로운 url 대한 설정
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET','POST']) # 회원가입 url 대한 설정
# methods에서 post를 설정해야지 회원가입시 다른 페이지로 넘어갈 수 있다.
# 기본 methods는 get이다.
def register():
    form = ReigistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        # 성공했을 경우 flash를 통해 해당 문구를 출력한다.
        return redirect(url_for('home')) # url_for는 함수명으로 호출하는 함수다.
    return render_template('register.html',title='Register', form=form)
    
@app.route('/login', methods=['GET','POST']) # 로그인 url 대한 설정
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            # 실패했을 경우 flash를 통해 해당 문구를 출력한다.
    return render_template('login.html',title='Login', form=form)