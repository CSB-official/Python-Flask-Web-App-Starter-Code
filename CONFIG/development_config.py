# IMPORT OS, USED TO FIND DB PATH
import os
from os.path import join, dirname, realpath

# DB-CONFIG
file_path = os.path.abspath(os.getcwd())+"/database.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
#SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/template1"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# MISC CONFIG
DEBUG = True
SECRET_KEY = "superrrrrrrr1234130123secretkey"
#SQLALCHEMY_POOL_SIZE = 2