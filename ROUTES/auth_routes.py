from flask import Blueprint, render_template, request, redirect, session
from flask_login import login_user, current_user, logout_user

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates')

@auth_blueprint.route("/auth_signin", methods=['GET', 'POST'])
def auth_signin():
    from models import db, User

    try:
        logout_user()
    except:
        print("No user to logout")

    if request.method == 'POST':

        if request.form.get('email', "") != "":

            if request.form.get('password', "") != "":
                user = User.query.filter_by(email = request.form.get('email', "").lower()).first()
                    
                    if user:
                        if user.password == request.form.get('password', ""):                            
                            
                            session['user_type'] = user.user_type
                            
                            login_user(user)
                            
                            current_user.most_recent_login = datetime.now()
                            current_user.total_num_logins = user.total_num_logins + 1
                            db.session.commit()

                            if current_user.user_type == "admin":
                                return redirect('/route_name_to_send_user_to_after_login')  
                    else:
                        message = "The combination of email and password do not match in our system, or the user does not exist. Please try again."
    
    return render_template('/AUTH-TEMPLATES/auth-signin.html', message = message)
