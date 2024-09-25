import random
from flask import Flask

# create a dict containing occupation info
def occupations_dict():
    occupations_str = open('occupations.csv').read()
    records = occupations_str.split('\n')
    records.pop(0)
    records.pop(-1) 
    records.pop(-1)

    occupations_info = {}
    
    for record in records:
        occupation, percentage = record.rsplit(',', 1)
        occupations_info[occupation] = float(percentage)
    return occupations_info

# select occupations 100 times based on the percentage weights
def random_selection(occupations_info, num):
    occupations = list(occupations_info.keys())
    percentages = list(occupations_info.values())
    return random.choices(occupations, weights=percentages, k=num)

app = Flask(__name__)

@app.route("/")

def occupation_chooser():
    team_name = "Maje_stic"
    roster = "Michelle Zhu, Jacob Lukose, Abidur Rahman, Evan Chan"
    occupation = random_selection(occupations_dict(), 1)[0]
    'the base language is HTML, so use <br> for line breaks'
    return team_name + "<br>" + roster + "<br>" + occupation + "<br>" + str(occupations_dict())

if __name__ == "__main__":    # true if this file NOT imported
    app.debug = True          # enable auto-reload upon code change
    app.run()
