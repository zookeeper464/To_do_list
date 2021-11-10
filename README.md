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
 - 회원가입한 내용을 db에 저장하는 방식에 대해서 이해한다.
 - 데이터가 충돌하는 경우에 대해서 에러 처리를 할 수 있도록 한다. 이를 forms에서 처리한다.
 (validate_(변수명) 참고)
 - request 모듈에 대해서 이해하고 활용할 수 있도록 추가 공부해야 한다.
 - login_user, current_user, logout_user, login_required에 대해서 이해하고 flask에서 활용할 수 있다.

7. html 상에서 이미지 처리를 어떻게 해야 하는지 방법에 대해서 공부하고 이해했다.
 - static파일 내부에 폴더를 만들어 해당 위치에서 데이터를 처리하도록 위치를 지정하고 해당 이미지를 html상에서 받을 수 있도록 처리했다.
 - account에서 새로운 값을 입력한다면 데이터를 수정하여 저장하고 만약 기존의 데이터가 들어온다면 에러를 출력하도록 한다.
 - enctype에 대해서 어떤 의미를 가진 html의 코드인지 알아봐야 한다.
 - flask_wtf.file 에서 파일을 어떻게 불러오고 어떤 파일만 제한적으로 가져오는지 이해한다.
 - secret모듈을 통해 데이터를 암호화하여 저장하는 방식을 이해한다.
 - os모듈의 함수를 통해 데이터를 저장하고 불러오고 위치를 지정하는 방식에 대해서 이해한다.
 - 받은 파일의 크기를 지정하여 저장할 수 있다.

8. CRUD를 활용하여 글을 저장한다.
 - db를 저장할 때 주의해야 하는 부분은 연결된 외래키의 경우, 연결된 backref의 이름을 활용해야 한다.
 - login_required는 로그인 여부를 판단해주고 로그인이 안된 경우, 호출이 안되도록 막는 것을 이해한다.
 - html에서 img태그 의 src는 주소를 의미하고 arc는 제목을 의미한다. 주소가 맞지 않으면 이미지가 깨지거나 오류가 발생한다.
 - 데이터가 없는데 찾으려 한다면 404를 띄우는 orm 쿼리 명령문 get_or_404(변수)를 이해한다.
 - <post_id>를 활용하면 post_id에 해당하는 데이터를 가져올 수 있다. <int:post_id>는 가져온 데이터를 정수형을 바꿔준다. 하지만 : 양쪽에 띄어쓰기를 해선 안된다.
 - flask의 모듈 abort를 통해 특정 오류를 띄울 수 있다. (403 등)
 - 부스트랩에서 가져온 html 모듈을 사용한다. (data-toggle='modal' data-target='#exampleModal')(example에 여러기능을 넣으면 된다. - 여기선 delete) (추가로 css를 넣으면 된다.)

9. paginate를 활용하여 데이터를 정렬하여 보여줄 수 있도록 한다.
 - request.args.get('page', 1, type=int)를 통해 데이터가 현재 1페이지에 있다는것을 저장한다.
 - Post.query.paginate(page=page,per_page=5)를 통해 데이터를 페이지당 5개를 보여주는 것을 저장한다.
 - query문에서 order_by()를 활용할 수 있다.
 - url에서 <>에 변수를 추가한다면 <>에 데이터타입:변수면을 넣고 함수 인자에 변수를 넣는다.
 - first_or_404는 get_or_404와 같이 데이터가 없을 경우 404 에러를 띄우는 함수다.

10. itsdangerous에서 암호화와 관련된 모듈을 공부하고 이해한다.
 - TimedJSONWebSignatureSerializer를 통해 데이터를 암호화하여 확인할 수 있다.
 - app.config['SECRET_KEY']를 설정하여 Serializer을 확인할 수 있다.
 - s.loads와 s.dumps를 활용하여 데이터의 일치여부를 확인하고 이해한다.
 - get_reset_token, verify_reset_token를 통해 user_id를 판단한다.
 - flask-mail은 conda에 설치되어 있지 않기 때문에 conda에서 가상환경을 관리하는 파일에 들어가 공식문서에 적힌대로 모듈을 다운받아 설치한다.
 - flask-mail을 통해 보내는 메일과 내용을 설정할 수 있다.
 - flask-mail을 활용하여 메일을 보내려고 했지만 오류가 발생한다. 검색하면 보안문제일 가능성이 매우 크다.
 (smtplib.SMTPSenderRefused: (530, b'5.7.0 Authentication Required. Learn more at\n5.7.0  https://support.google.com/mail/?p=WantAuthError ne22sm3150197pjb.18 - gsmtp', 'noreply@demo.com'))

11. bluepoint를 활용하여 코드를 깔끔하게 정리하고 관리하기 쉽게 만든다.
 - bluepoint를 활용하여 forms,routes를 각각 다른 파일에서 관리할 수 있도록 저장한다.
 - bluepoint를 활용할 수 있도록 기존의 db,flask,bcrypt,login_manager,email 등 변수를 작성하는 방법을 이해한다.
 - flask의 환경설정을 저장할 수 있는 config.py를 생성하여 환경설정 내용을 따로 관리할 수 있도록 한다.

 - AttributeError: 'NoneType' object has no attribute 'drivername' 라는 에러가 나면서 /home을 호출할때 Post의 내용을 가져올 수 없다고 나온다. => 내용이 바뀐것이 없기 때문에 변수가 틀렸다고 생각한다.
 - RuntimeError: A secret key is required to use CSRF. 라는 에러가 나면서 /login, /register를 호출할 수 없다고 나온다. => config.py가 문제일 것이라고 생각한다.