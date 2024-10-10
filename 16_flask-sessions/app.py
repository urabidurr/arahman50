# Abidur Rahman
# SoftDev
# October 8 2024
#Time Spent: 0.5 hrs

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

app.secret_key = os.urandom(32)

'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET', 'POST'])
# Prediction: This should work fine as long as the login.html file exists
# in a templates folder. If the file is missing, Flask will
#throw an error. reused old code
def disp_loginpage():
    print("printed")
    return render_template( 'login.html' )


@app.route("/auth",  methods=['GET', 'POST'])
# Prediction: This will work if the form submits via GET request and
#includes a username argument. If the form uses POST,
#or if the username field is missing, this will throw an error. reusewd old code
def authenticate():
    if request.method == 'GET':
        user = request.args['username']
        password = request.args['password']
        session[app.secret_key] = password
    elif request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        print(user, password)
        session[app.secret_key] = password
    else:
        return "error!"
    return render_template('response.html', user = user) 


@app.route("/logout",  methods=['GET', 'POST'])
def logout():
if request.method == 'GET':
    print("received GET")
    session.pop(app.secret_key)
    print(session)
else if request.method == 'POST':
    print("received POST")
    session.pop(app.secret_key)
    print(session)
    
    
    
if __name__ == '__main__':
    app.debug = True
    app.run()
    
