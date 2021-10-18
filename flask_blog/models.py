from datetime import datetime
from flask_blog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    # User 테이블에 컬럼에 대한 설정이다.

    posts = db.relationship('Post', backref='author', lazy=True)
    # User테이블과 Post테이블을 연결하는 변수설정
    # 연결하기 위한 변수명, 그 내부에는 연결하고자하는 테이블명, backref등이 필요하다.

    def __repr__(self): # User 테이블의 표현에 대한 함수
        return f"User ('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # backref시 연결을 알려주기 위해 db.Foreignkey('테이블.주요키')를 설정해야 한다.
    # Post 테이블에 컬럼에 대한 설정이다.

    def __repr__(self): # Post 테이블의 표현에 대한 함수
        return f"Post ('{self.title}','{self.date_posted}')"