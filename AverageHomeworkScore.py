from dotenv import load_dotenv
import pymongo
import os
import statistics
import matplotlib.pyplot as plt
import seaborn

#Loading environment variables
load_dotenv(dotenv_path="CS125.env")
database_url = os.environ.get("CS125MONGO")

#Connecting to the database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

#A list of every collection present
field_best = list(db.best.find())

def getMeanHomeworkScores():

    homework_numbers = []
    #Finds all of the homework for that semester
    for key in field_best[0]['homework']:
        if key[0:2] == "HW":
            homework_numbers.append(int(key[2:]))

    final_scores = {}

    for homework in homework_numbers:

        #Appends the current lab number to finish the string
        current_homework = "HW%s" % (str(homework))
        current_homework_scores = []

        for document in field_best:
            current_homework_scores.append(document['homework'][current_homework]['score'])

        mean = statistics.mean(current_homework_scores)
        final_scores[current_homework] = mean

    return final_scores

scores = getMeanHomeworkScores()
x = list(scores.keys())
y = list(scores.values())

bars = plt.bar(x, y)
plt.xticks(x, x, rotation=90)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 1, int(round(yval, 1)))

plt.plot()
plt.show()



