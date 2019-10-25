import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '29402edaa55266d3b2dd97060fc79c34f6d6763db8740e8819fca170fd1b7a0f'
    CLIENT_ID = 'sUqkVCSvxQOTq7PYFNMhoB52'
    CLIENT_SECRET = 'tGpmct3lSvSm9YOtM8j00CFWZDg78ASK'
    JSON_AS_ASCII = False
    ACCESS_TOKEN = ''
    UPLOADED_PHOTOS_DEST = os.getcwd() + '/img'
    FLASK_MAIL_SUBJECT_PREFIX = '[Patrick]'
    FLASK_MAIL_SENDER = 'Patrick <{}>'.format(os.environ.get('MAIL_USERNAME'))
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_PORT = 25  # SSL，TLS都不要开...就是这个端口了
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PASSWORD = 'ec3c51ababe8d311'


class ProdConfig(Config):
    debug = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod.sqlite')
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:patrickcty@localhost/debugdidi'


class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    SQLALCHEMT_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
    SQLALCHEMT_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
