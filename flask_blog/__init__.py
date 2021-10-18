from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Flask는 기본 앱을 실행하기 위한 웹 변수
# __init__.py 파일 과 templates 폴더는 같은 위치에 존재해야 한다.

app = Flask(__name__) # 가장 기본적인 flask 앱 설정

app.config['SECRET_KEY'] = 'd41aadc3731760a044e2ad22097f44df' # flask app에 대한 환경설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # flask 의 데이터베이스 연결되는 주소를 설정
app.config['FLASK_DEBUG'] = 1

db = SQLAlchemy(app) # db와 flask를 연결하는 과정

from flask_blog import routes