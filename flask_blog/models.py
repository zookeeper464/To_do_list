from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin

from flask_blog import db, login_manager

@login_manager.user_loader # 유저가 있다면 불러오는 과정에 대한 설정
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    # User 테이블에 컬럼에 대한 설정이다.

    posts = db.relationship('Post', backref='author', lazy=True)
    # User테이블과 Post테이블을 연결하는 변수설정
    # 연결하기 위한 변수명, 그 내부에는 연결하고자하는 테이블명, backref등이 필요하다.

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
        # 암호화된 비밀키 생성하고 return
        
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try: user_id = s.loads(token)['user_id']
        except: return None

        return User.query.get(user_id)
        # 더미 데이터가 맞는지 틀린지 확인한다.

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
        return f"Post('{self.title}', '{self.date_posted}')"    