import uuid
import datetime
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask_uploads import UploadSet, IMAGES

db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)


class Verify:

    """Verify when password is forgotten."""

    @staticmethod
    def generate_confirmation_token(nickname, email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'nickname': nickname, 'email': email})

    @staticmethod
    def confirm(token, nickname, email):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('nickname') != nickname or data.get('email') != email:
            return False
        return True


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(36), default=lambda: str(uuid.uuid4()))
    nickname = db.Column(db.String(128), unique=True)
    avatar_url = db.Column(db.String(256), default='https://static.jnugeek.cn/img/avatar.jpg')
    passwd = db.Column(db.String(128))
    sex = db.Column(db.Enum('男', '女'))
    hobby = db.Column(db.String(256))
    birth_date = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    confirmed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    @property  # 只读函数
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.passwd = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passwd, password)

    evaluations = db.relationship(
        'Comment',
        backref='user',
        lazy='dynamic'
    )

    def generate_auth_token(self, expiration=3600 * 24):  # 时间单位是秒
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id, 'uid': self.uid})

    @staticmethod
    def verify_auth_token(token):
        if not token:
            return None

        s = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = User.query.get(data['id'])
        if user.uid != data['uid']:
            return None
        return user

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.email})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.email:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer)
    content = db.Column(db.Text)
    cred_at = db.Column(db.DateTime, default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
