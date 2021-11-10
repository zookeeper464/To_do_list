from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_blog.config import Config
# Flask는 기본 앱을 실행하기 위한 웹 변수
# __init__.py 파일 과 templates 폴더는 같은 위치에 존재해야 한다.

db = SQLAlchemy() # db를 변수로 생성하는 과정
bcrypt = Bcrypt() # 플라스크 암호화 과정을 추가하기 위한 과정
login_manager = LoginManager() # 플라스크 로그인 과정을 추가하기 위한 과정
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
# 데이터가 없는 상황에서 잘 못들어갔다면 error로 처리하고 login페이지로 이동하는 설정
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__) # 가장 기본적인 flask 앱 설정
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # 위에서 설정했던 변수들과 flask를 연결하는 과정

    from .users.routes import users
    from .posts.routes import posts
    from .main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app

    # app.config['SECRET_KEY'] = 'd41aadc3731760a044e2ad22097f44df' # flask app에 대한 환경설정
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # flask 의 데이터베이스 연결되는 주소를 설정
    # app.config['FLASK_DEBUG'] = 1

    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    # 메일을 보내기위한 준비단계(환경설정)