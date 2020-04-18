import seaborn
from dotenv import load_dotenv
import pymongo
import os
import statistics
import matplotlib.pyplot as plt

#Loading environment variables
load_dotenv(dotenv_path="CS125.env")
database_url = os.environ.get("CS125MONGO")

#Connecting to the database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

#A list of every collection present
field_best = list(db.best.find())

def getMeanLabScores():

    lab_numbers = []
    #Finds all of the labs for that semester
    for key in field_best[0]['homework']:
        if key[0] == "L":
            lab_numbers.append(int(key[1:]))

    final_scores = {}

    for lab in lab_numbers:

        #Appends the current lab number to finish the string
        current_lab = "L%s" % (str(lab))
        current_lab_scores = []

        for document in field_best:
            current_lab_scores.append(document['homework'][current_lab]['score'])

        mean = statistics.mean(current_lab_scores)
        final_scores[current_lab] = mean

    return final_scores

scores = getMeanLabScores()

x = list(scores.keys())
y = list(scores.values())
barplot = seaborn.barplot(x, y)
bars = plt.bar(x, y)


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 1, round(yval, 2))

plt.plot()
plt.show()



