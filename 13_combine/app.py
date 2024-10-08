"""
Andy Shyklo, Ankita Saha, Abidur Rahman
Python Pigs
SoftDev
K12 - templates more w/ occupations.csv
2024-09-27
time spent: 1 hr
"""

from flask import Flask, render_template
import csv, random
app = Flask(__name__)

coll = [1,2,3,4]
CSV_FILE_PATH = "data/occupations.csv"

def fileParser(file): #reads csv
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')
        data = []
        for line in csvFile:
            data.append(line)
    return data

def splitHeaders(dataSet): #converts data to dictionary
    dictValues = {}
    for data in dataSet:
        for string in data:
            three = string.rsplit(',', 2)
            if len(three) == 3 and three[1].replace('.', '', 1).isnumeric():  
                job = three[0]
                percentage = float(three[1])
                link = three[2]
                dictValues[job] = [percentage, link] 
                    
    return dictValues

def randomizeJob(dict): #randomizes job, weighted
    randVal = random.uniform(0,99.8)
    for data in dict:
        print(data)
        randVal -= (dict[data])[0]
        if(randVal <= 0):
            return data

@app.route("/wdywtbwygp")
def hello_world():
    global CSV_FILE_PATH
    jobData = fileParser(CSV_FILE_PATH)
    headers = jobData[0][0].split(',')
    numJobData = jobData[1:len(jobData)-1] #not counting the header of the values + the total amount
    dictValues = splitHeaders(numJobData)
    #print(dictValues)
    random = randomizeJob(dictValues)
    
    return render_template('tablified.html', foo="Python Pigs", heading="app.py for app reoute of wdywtbwygp", roster="Python Pigs: Andy Shyklo, Ankita Saha, Abidur Rahman", dictValues=dictValues, random=random)

if __name__ == "__main__":
    app.debug = True
    app.run()
