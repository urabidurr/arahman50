from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/', methods = ['GET', 'POST'])
def dispHTML():
    return render_template("style.html")

if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
