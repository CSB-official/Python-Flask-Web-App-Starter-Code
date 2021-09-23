from models import *
# DATA LOADERS
# This file is used for pythonic object creation within your database
# THIS IS NOT A REQUIRED FILE FOR YOUR APPLICATION. To use this application, via terminal:
# Navigate to this directory
# Python3
# from load_db import *
# load_tasks()
# ^ You will now have a sqlite DB created with sample user added
#############################################################################

# Add sample user to DB with Admin permission
def create_db_and_user():

    db.create_all()
    db.session.commit()

    admin_user = User(
        organization_id = 0,
        first_name = 'Connor',
        last_name = 'Brady',
        user_type = 'admin',
        email = 'connor@reflectlabs.io',
        phone_number = '1234567890',
        password = 'password',
    )
    db.session.add(admin_user)
    db.session.commit()

    print('********************* DB CREATED *********************')
    return "load successful"

def load_tasks():

    from time import time
    from app import db
    print('********************* STARTING SPECIFIED LOAD TASKS *********************')

    t = time()
    
    db.drop_all()
    db.session.commit()
    create_db()
    create_db_and_user()
    db.session.close()

    print('********************* LOAD TASKS COMPLETE *********************')
    print("Total elapsed time: " + str(time() - t) + " s.")