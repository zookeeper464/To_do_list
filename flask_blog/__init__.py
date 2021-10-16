from flask import Flask, render_template
# Flask는 기본 앱을 실행하기 위한 웹 변수
# reder_template는 flask에서 html을 호출하기 위한 모듈
# __init__.py 파일 과 templates 폴더는 같은 위치에 존재해야 한다.

app = Flask(__name__) # 가장 기본적인 flask 앱 설정

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
def hello():
    return render_template('home.html', posts=posts)
    # posts는 python에서 html로 보내는 변수를 의미한다.
    # posts가 아닌 다른 변수명을 활용하여 html에서 받아도 상관없다.

@app.route('/about') # 새로운 url 대한 설정
def about():
    return render_template('about.html',title='About')