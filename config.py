import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+mysql://pwlresponsi_belongbite:a33f82fe60054555fd463fcc0a724f4138cb2f33@zp6.h.filess.io:3307/pwlresponsi_belongbite'

SQLALCHEMY_TRACK_MODIFICATIONS = False
