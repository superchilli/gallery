# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "a very compalicated key"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    GALLERY_MAIL_SUBJECT_PREFIX = '[GALLERY]'
    GALLERY_MAIL_SENDER = 'somelovebg@hotmail.com'
    GALLERY_ADMIN = 'rose@cute.com' or os.environ.get('ADMIN')
    UPLOADED_PHOTO_DEST = os.getcwd() + '/app/static/img/'
    GALLERY_COMMENTS_PER_PAGE = 15
    GALLERY_PHOTOS_PER_PAGE = 20
    GALLERY_PHOTO_LIKES_PER_PAGE = 20
    GALLERY_FOLLOWERS_PER_PAGE = 10
    BOOTSTRAP_SERVE_LOCAL = True


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG =True
    MAIL_SERVER = 'smtp.live.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')



config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

