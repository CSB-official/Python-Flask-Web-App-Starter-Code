import os

# DB-CONFIG
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

# MISC CONFIG
DEBUG = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "superrrrrrrr1234130123secretkey"
#SQLALCHEMY_POOL_SIZE = 2