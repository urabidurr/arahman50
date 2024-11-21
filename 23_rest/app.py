# Team Astros
# Andy Shyklo and Abidur Rahman
# November 20, 2024
# 30 minutes

import urllib.request, json
from flask import render_template, Flask, session, request, redirect

f = open("key_nasa.txt")
key = f.read()

app = Flask(__name__)    #create Flask object
app.secret_key = b'_5#j812jwwjkKLWio)2u'

@app.route("/")
def root():
    request_url = urllib.request.urlopen(f'https://api.nasa.gov/planetary/apod?api_key={key}')
    readUrl = request_url.read()

    x = json.loads(readUrl[:-1])
    image1 = x["url"]

    return render_template("main.html", image1=image1)

if __name__ == "__main__":
    app.debug = True 
    app.run()
