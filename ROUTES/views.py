# Base app imports
from app import app

# Flask Imports
from flask import Flask, redirect, session, request, render_template, jsonify
from werkzeug.exceptions import HTTPException
from flask_login import login_user, current_user, login_required


# WEBSITE ROUTES 
#############################################################################

# Redirects your base '/' route to the login route (optional)
@app.route("/", methods=['GET', 'POST'])
def website():
    return redirect('/auth_signin')

# ERROR HANDLERS (optional)
#############################################################################
@app.errorhandler(404)
def page_not_found(error):

    print(error)
    return redirect('/')


@app.errorhandler(401)
def page_not_found(error):

    print(error)
    return redirect('/')


@app.errorhandler(500)
def page_not_found(error):

    print(error)
    return redirect('/')


@app.errorhandler(401)
def custom_401(error):
    print("Unauthorized")
    return render_template('/AUTH-TEMPLATES/auth-signin.html', message = "Authorization failed!")


@app.errorhandler(Exception)
def handle_error(e):
    print("current user")
    print(current_user)
    print("Error Handler: " + str(e))

    code = 500

    if isinstance(e, HTTPException):
        code = e.code

    session['user_error_message'] = 'on'

    print(jsonify(error=str(e)), code)
    print("current user")
    print(current_user)

    if not current_user:
        return redirect('/')

# MISC FUNCTIONS
#############################################################################
def close(self):
    self.session.close()
    self.db.dispose()