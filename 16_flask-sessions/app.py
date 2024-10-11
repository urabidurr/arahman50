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
import secrets


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = secrets.token_hex(16) # setting a key to secret key


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
    if 'username' in session:
        return render_template('response.html', username=session['username'], pass1=session['password'])
    return render_template('login.html')

@app.route("/auth",  methods=['GET', 'POST'])
# Prediction: This will work if the form submits via GET request and
#includes a username argument. If the form uses POST,
#or if the username field is missing, this will throw an error. reusewd old code
def authenticate():
    if request.method == 'GET':
        user = request.args['username']
        pass1 = request.args['password']
        session['username'] = user
        session['password'] = pass1
    elif request.method == 'POST':
        user = request.form.get('username')
        pass1 = request.form.get('password')
        session['username'] = user
        session['password'] = pass1
    else:
        return "error!"
    return render_template('response.html', user = session['username'], pass1 = session['password']) 

def disp_logoutpage():
    if request.method == 'GET':
        user = request.args['username']
        pass1 = request.args['password']
        session['username'] = user
        session['password'] = pass1
    elif request.method == 'POST':
        user = request.form.get('username')
        pass1 = request.form.get('password')
        session['username'] = user
        session['password'] = pass1
    else:
        return "error!"
    return render_template('response.html', user = session['username'], pass1 = session['password']) 

if __name__ == '__main__':
    app.debug = True
    app.run()
    
