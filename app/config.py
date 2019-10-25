import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '29402edaa55266d3b2dd97060fc79c34f6d6763db8740e8819fca170fd1b7a0f'
    CLIENT_ID = 'sUqkVCSvxQOTq7PYFNMhoB52'
    CLIENT_SECRET = 'tGpmct3lSvSm9YOtM8j00CFWZDg78ASK'
    JSON_AS_ASCII = False
    ACCESS_TOKEN = ''
    UPLOADED_PHOTOS_DEST = os.getcwd() + '/img'
    APPID = 'wxb29b3d8ad9b05c5a'
    APP_SECRET = '38890f5c42abad41c1ddd4eaef18a8bb'


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
