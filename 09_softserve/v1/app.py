# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route, meaning the function will be called upon accessing the http://localhost:5000/
def hello_world():
    return "No hablo queso!"

app.run()    #Starts the local host server to run and display the function

#Instead of printing __name__, the function hello_world() only returns a string "No hablo queso!".
