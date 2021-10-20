from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from PIL import Image
from flask_blog import app, bcrypt, db
from .forms import ReigistrationForm, LoginForm, UpdateAccountForm
from .models import User, Post
import secrets, os

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
    if current_user.is_authenticated: # 현재 유저가 있는지 확인하는 조건문
        return redirect(url_for('home'))

    form = ReigistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # 비밀번호를 bccrypt를 통해 암호화한 뒤에 데이터를 db에 저장한다.
        flash('Your account has been created! You are now able to log in','success')
        # 성공했을 경우 flash를 통해 해당 문구를 출력한다.
        return redirect(url_for('login')) # url_for는 함수명으로 호출하는 함수다.

    return render_template('register.html',title='Register', form=form)
    
@app.route('/login', methods=['GET','POST']) # 로그인 url 대한 설정
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next') # 요청되었던 원래 페이지를 호출하는 변수
            if next_page:
                return redirect(next_page) # 원래 호출하려던 페이지가 있다면 그 페이지를 호출
            else:
                return redirect(url_for('home')) # 아니라면 원래 home을 호출

        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
        # 실패했을 경우 flash를 통해 해당 문구를 출력한다.

    return render_template('login.html',title='Login', form=form)

    
@app.route('/logout') # 로그아웃 url 대한 설정
def logout():
    logout_user() # 로그아웃 해주는 함수
    return redirect(url_for('home'))

def save_picture (form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    # 그림 데이터를 가져와 파일과 경로를 지정하는 과정
    
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # 크기를 작게 만들어 섬네일을 저장하는 과정
    i.save(picture_path)

    return picture_fn

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been update!', 'success')
        return redirect(url_for('account'))
    
    # 데이터를 새롭게 받았다면 기존의 데이터를 새로운 데이터로 변경한다.
    # 기존의 데이터는 역시나 삭제된다.
    # 이미 존재하는 데이터로 바꾸려고 한다면 이를 에러처리한다. (form에 나온다.)
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    return render_template('account.html',title='Account', 
                            image_file=image_file, form=form)