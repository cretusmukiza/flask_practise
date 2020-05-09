class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/practise'
    JWT_SECRET_KEY = 'zzzzz-xxxx-0000'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/practise'

class TestingConfig(Config):
    DEBUG = True  
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False


