class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/author'
    JWT_SECRET_KEY = 'zzzzz-xxxx-0000'
    SECRET_KEY = 'MEWMF-3034-121OD'
    SECURITY_PASSWORD_SALT = 'MEO@@@@288****'
    MAIL_DEFAULT_SENDER = 'SENDER-EMAIL'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'SENDER-EMAIL'
    MAIL_PASSWORD = 'SENDER-EMAIL-PASSWORD'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/practise'

class TestingConfig(Config):
    DEBUG = True  
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False


