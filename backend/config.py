import os
from datetime import timedelta

class Config:
    """_General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:12345@localhost/quickmed'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)


class TestConfig(Config):
    
    pass


class ProdConfig(Config):
    '''
Production  configuration child class

Args:
    Config: The parent configuration class with General configuration settings
'''
    pass


class DevConfig(Config):
    '''
Development  configuration child class

Args:
    Config: The parent configuration class with General configuration settings
'''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
