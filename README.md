# To_do_list
플라스크 기본 활용 개념을 위한  체크리스트 페이지 생성

1. Flask모듈과 route에 관한 이해에 대해서 공부하고 사용하는 방법을 이해했다.

2. render_template모듈과 html에서 extends, block과 파이썬에 대한 문법에 대해서 공부하고 사용하는 방법을 이해했다.
 - extends, block은 중복된 html 서식에 대해서 불필요한 중복을 피할 수 있도록 돕는 역할을 한다.
 - 부스트트랩 문서 주소 : https://getbootstrap.com/docs/5.1/getting-started/introduction/
 - 문서를 꾸미는 css의 경우 static파일을 활용한다.
 - <link rel='stylesheet' type='text/css', href="{{ url_for('static',filename='main.css') }}"> 을 활용하여 가져온다. type을 통해 설정 href를 통해 주소를 설정한다.
 - 어떤 css를 활용하고 가져올지는 백엔드 개발자를 목표로 하기 때문에 다음으로 미루고 기존에 사용되는 형태의 css를 가져와 활용하도록 한다.

3. flask_wtf모듈에서 로그인과 관련된 기능에 대해서 공부하고 이해했다.
 - FlaskForm은 class 형태로 flask의 기능을 가져오기 위해서 상속하는 용도로 사용한다.
 - wtforms 에서 변수를 다룬다.(StringField, validators.DataRequired)
 - 모르는 모듈의 함수 내용에 대해서 이해할 수 있게 되었다.(dir(),help()를 활용한다.)