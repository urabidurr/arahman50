# Michelle Zhu, Jacob Lukose, Abidur Rahman, Evan Chan
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             # create instance of class Flask

@app.route("/")                   # assign fxn to route
def hello_world():
    print("about to print __name__...") # this prints right above "__main__"
    print(__name__)               # this prints in the terminal
    return "No hablo queso!"

app.run()
