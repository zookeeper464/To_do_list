from flask import url_for, current_app
from flask_mail import Message
from PIL import Image

from flask_blog import mail
import os, secrets

def save_picture (form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    # 그림 데이터를 가져와 파일과 경로를 지정하는 과정

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # 크기를 작게 만들어 섬네일을 저장하는 과정
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
            sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)