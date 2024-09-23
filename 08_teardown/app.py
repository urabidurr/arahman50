'''Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  Running Flask scripts and making observations
  2024-9-21
  time spent: 0.67 hours
  '''

'''
DISCO:
<note any discoveries you made here... no matter how small!>
-We noticed that the return is what is printed on the content of the webpage itself, but the print function doesn't really do anything on the front end -- we're assuming it's going into the backend to create the webpage
-We think the print(__name__) points to the specific part of the app.
-print statements only show up after you close the webpage (on the console) -- weird b/c return is after the print (? strange)
-runs in a webpage
-internally generates html code as well
-runs locally
-you can run the virtual environment from even outside the directory/virtual env
-py works instead of python too

QCC:
0. What is __name__ referring to? Is it something built-in already?
1. Why does the app need to be put in the root if that is the case? 
2. What is the Flask() doing? Is it just creating the object for the app?
3. Why is there print and return? Usually return overrides print but what are both of them doing here in this case?
4. Where the hello_world get run? What is happening internally when you run the program?
5. DO you always have to run .run() to get the webpage up?
 ...

INVESTIGATIVE APPROACH:
So first we tried to understand the code just by looking through each line and noting any similarities we saw with other languages, etc. After writing our QCCs, we tried to run the script. We did this with the same approach from class on Friday, where we created a virtual environment to run the script and install flask. We got a warning that had a link to the localhost. we went to that link and noted our new observations. we tinked around a bit -- we did CTRL-C to see where that leads us too and if there are any changes in the console or webpage. AFter some explorations, we messed around w/ the values for the different parameters to see what would happen. we then wrote our discoveries.
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs? A: One thing we noticed is that the @app.route is similar to the @override in Java.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?  A: From what we know "/" refers to the root directory so we think it is putting the app in the root directory or searching for it there; or it is going to the root direectory of the app and running it from there.
def hello_world():
    print(__name__)                      # Q2: Where will this print to?Q3: What will it print? A: It creates the webpage, perhaps it is the https response thats goes into the localhost
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know? A: Yes, this appears on the webpage of the my local link that was given when I ran the script. It prints "No hablo queso!"

app.run()                                # Q5: Where have you seen similar constructs in other languages? A: I think Java uses a similar construct. Different javascript programs like Node.js and React.js have similar aspects as well.


