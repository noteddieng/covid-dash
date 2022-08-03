from os import environ
from os import path 
from dotenv import load_dotenv

class Config:

    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))

    # Fill in later with Secret Key, Cookies, anything else

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    # Add databse URI later

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    # add database URI later