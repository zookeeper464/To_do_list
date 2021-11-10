from flask import render_template, request, Blueprint
from flask_blog.models import Post

main = Blueprint('main', __name__)

@main.route('/') # 기본인덱스에 대한 설정
@main.route('/home') # route는 여러개 설정해도 좋다.
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    # posts는 python에서 html로 보내는 변수를 의미한다.
    # posts가 아닌 다른 변수명을 활용하여 html에서 받아도 상관없다.

@main.route('/about') # 새로운 url 대한 설정
def about():
    return render_template('about.html',title='About')
