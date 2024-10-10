'''Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  Running Flask scripts vs. html scripts
  2024-9-25
  time spent: 0.67 hours
'''

# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())

'''
@app.route("/static/fixie.html")
def hi():
    print("the __name__ of this module is... ")
    print(__name__)
    return "<h1>Team Name: Python Pigs</h1><br><h2>Roster: Ankita Saha, Andy Shyklo, Abidur Rahman</h2>"
'''
    
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
