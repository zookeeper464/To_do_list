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
 - 동일 파일 내부에서 다른 파일의 클래스를 호출하려면 from .(파일명) import (클래스)를 사용한다.
 - div에서 class에 따라서 내용이 달라지는 것을 기억하고 나중에 전달할 때 헷갈리지 않도록 주의한다.(단순하게 class가 데이터를 분류하는 작업만 하는 것이 아니다.)
 - url_for(함수명) 임을 기억하고 활용할 수 있도록한다.
 - class=form-control-label,form-check-input,form-check-label,btn btn-outline-info 등 변수명의 의미를 이해해야 한다.(아직 검색하지 않았다.)
 - flash를 통해 해당 작업에 대한 결과를 확인할 수 있게 만들 수 있다.(post 작업시 주로 활용된다.)

4. flask_sqlalchemy모듈에서 db를 생성하고 db를 구성하는 방법에 대해서 공부하고 이해했다.
 - db.session.add(입력 컬럼내용),db.session.commit() -git과 유사 등과 같은 명령어에 대해서 이해한다.
 - (테이블명).query.all(), (테이블명).query.first(), (테이블명).query.(쿼리 명령어).all(), (테이블명).query.(쿼리 명령어).first() 등 명령어에 대해서 이해한다.
 - 쿼리 명령어는 filter_by(컬럼명='원하는 내용')
 - (테이블명).query.get(num) 해당 쿼리문의 데이터 중 num번째 데이터를 가져온다.
 - 관계를 나타내는 변수를 query문으로 호출할때는 관련된 내용이 리스트의 형태로 출력된다.
 - backref가 author이므로 query문으로 호출한 데이터의 작가를 알고 싶다.면 (데이터).author를 사용한다.
 - db.Column, db.create_all(), db.drop_all()

6. flask_bcrypt모듈에서 데이터를 해시로 확인할 수 있는 방법에 대해서 공부하고 이해했다.
 - from flask_bcrypt import Bcrypt, bcrypt = Bcrypt(), hash_code = bcrypt.generate_password_hash('string'), hash_code.decode('utf-8'), bcrypt.check_password_hash(hash_code.decode('utf-8),'string')이 어떤 방식으로 동작하는지 이해한다.
 