# Base imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os
import sys

# Use Flask Blueprints to seperate your application into seperate python files. These are two example blueprints in the 'ROUTES' directory. 
from ROUTES.admin_routes import admin_blueprint
from ROUTES.customer_settings_routes import customer_settings_blueprint


####### VERIFY IF DEPLOYED OR NOT #######
# This variable enabled different configs for local and deployed enviornments. Review /CONFIG/deployed and /CONFIG/local
# This also enables and disables debug mode automatically
is_deployed = True
####### VERIFY IF DEPLOYED OR NOT #######


# Build Python App
app = Flask(__name__)

# Init DB
db = SQLAlchemy(app)

# YOU MUST REGISTER YOUR IMPORTED BLUEPRINTS
app.register_blueprint(admin_blueprint)
app.register_blueprint(customer_settings_blueprint)


# Config switcher
# 0AUTHLIB_INSECURE_TRANSPORT = 1 is optional / part of the oauth library for local development
if is_deployed == True:
    app.config.from_pyfile(os.path.abspath(os.getcwd()) + '/CONFIG/deployed_config.py')
else:
    app.config.from_pyfile(os.path.abspath(os.getcwd()) +  '/CONFIG/development_config.py')
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Import all of views
from ROUTES.views import *

# Config Login Manager w/ a User Loader
login_manager = LoginManager()
login_manager.init_app(app)

# The login_manager handles authenticating users at login. Visit auth_routes for more information on authenticating and logging in users
# Technically you only need the following code, the code after the comment below includes starter code around permision based login (Admin being redirected to a different route, for example):
'''
@login_manager.user_loader
def load_user(user_id):
from models import db, User
    return User.query.get(int(user_id))

'''
@login_manager.user_loader
def load_user(user_id):
    from models import db, User
    try:
        if session['user_type'] == 'admin':
            return User.query.get(int(user_id))
        else:
            return None
    except:
        return None

if __name__ == "__main__":
    # Optional Jinja Cache settings enabled. Simply comment out or remove app.jinja_env.cache = {}
    app.jinja_env.cache = {}
    # Run app
    app.run(debug=app.config['DEBUG'])