import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://apisia_batmarried:5ef07a2f5aa793451403907e6670280a6167877e@0nn.h.filess.io:3307/apisia_batmarried'

SQLALCHEMY_TRACK_MODIFICATIONS = False