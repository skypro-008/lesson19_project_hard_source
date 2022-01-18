class Config(object):
    DEBUG = None
    SECRET_HERE = None


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(dev=DevelopmentConfig)
