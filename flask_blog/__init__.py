from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# Flask는 기본 앱을 실행하기 위한 웹 변수
# __init__.py 파일 과 templates 폴더는 같은 위치에 존재해야 한다.

app = Flask(__name__) # 가장 기본적인 flask 앱 설정

app.config['SECRET_KEY'] = 'd41aadc3731760a044e2ad22097f44df' # flask app에 대한 환경설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # flask 의 데이터베이스 연결되는 주소를 설정
app.config['FLASK_DEBUG'] = 1

db = SQLAlchemy(app) # db와 flask를 연결하는 과정
bcrypt = Bcrypt(app) # 플라스크 암호화 과정을 추가하기 위한 과정
login_manager = LoginManager(app) # 플라스크 로그인 과정을 추가하기 위한 과정
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' # 데이터가 없는 상황에서 잘 못들어갔다면 error로 처리하고 login페이지로 이동하는 설정

from flask_blog import routes