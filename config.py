import os


class Config(object):
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True



class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False
    HOST = '0.0.0.0'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False
