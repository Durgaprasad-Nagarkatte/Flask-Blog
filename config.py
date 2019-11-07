import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-forget'
    RECAPTCHA_PUBLIC_KEY = "6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///" + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False