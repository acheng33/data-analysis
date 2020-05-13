from dotenv import load_dotenv
import pymongo
import os
import statistics
import matplotlib.pyplot as plt

#Loading environment variables
load_dotenv()
database_url = os.environ.get("CS125MONGO")

#Connecting to the database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

#A list of every collection present in best
field_best = list(db.best.find())

def getMeanLabScores():

    lab_numbers = []
    #Finds all of the labs for that semester
    for key in field_best[0]['homework']:
        if key is not None and key[0] == "L":
            lab_numbers.append(int(key[1:]))

    final_scores = {}

    for lab in lab_numbers:
        if lab is not None:
            #Appends the current lab number to finish the string
            current_lab = "L%s" % (str(lab))
            current_lab_scores = []

            for document in field_best:
                if document is not None:
                    #Appends the scores for that lab
                    current_lab_scores.append(document['homework'][current_lab]['score'])

            mean = statistics.mean(current_lab_scores)
            final_scores[current_lab] = mean

    return final_scores

scores = getMeanLabScores()

x = list(scores.keys())
y = list(scores.values())

colors = {1 : 'darkgreen', 2 : 'royalblue'}
bar_colors = []
is_green_bar = True

#Alternates bar colors
for value in x:
    if is_green_bar:
        bar_colors.append(1)
        is_green_bar = False
    else:
        bar_colors.append(2)
        is_green_bar = True

bars = plt.bar(x, y, edgecolor='black', color=[colors[elem] for elem in bar_colors])

#Assigns the average score above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 1, round(yval, 2))

plt.title("Average Lab Scores")
plt.xlabel("Lab Assignments")
plt.ylabel("Scores")
plt.plot()
plt.savefig("Lab_Score_Distributions.png")
plt.show()



