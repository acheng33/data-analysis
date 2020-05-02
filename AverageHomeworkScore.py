from dotenv import load_dotenv
import pymongo
import os
import statistics
import matplotlib.pyplot as plt


#Loading environment variables
load_dotenv(dotenv_path=".env")
database_url = os.environ.get("CS125MONGO")

#Connecting to the database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

#A list of every collection present in the best field
field_best = list(db.best.find())

def getMeanHomeworkScores():

    homework_numbers = []
    #Finds all of the homework names for that semester
    for key in field_best[0]['homework']:
        if key[0:2] == "HW":
            homework_numbers.append(int(key[2:]))

    final_scores = {}

    for homework in homework_numbers:
        if homework is not None:
            #Appends the current lab number to finish the string
            current_homework = "HW%s" % (str(homework))
            current_homework_scores = []

            for document in field_best:
                if document is not None:
                    #Appends every homework score for the current homework
                    current_homework_scores.append(document['homework'][current_homework]['score'])

            mean = statistics.mean(current_homework_scores)
            final_scores[current_homework] = mean

    return final_scores

scores = getMeanHomeworkScores()
x = list(scores.keys())
y = list(scores.values())

colors = {1 : 'darkolivegreen', 2 : 'teal'}
bar_colors = []
is_green_bar = True

#Alternates the bar's color
for value in x:
    if is_green_bar:
        bar_colors.append(1)
        is_green_bar = False
    else:
        bar_colors.append(2)
        is_green_bar = True

bars = plt.bar(x, y, edgecolor='black', color=[colors[elem] for elem in bar_colors])

plt.xticks(x, x, rotation=90)

figure = plt.gcf()
figure.set_size_inches(14, 10.8)
plt.title("Average Homework Scores")
plt.xlabel("Homework Assignments")
plt.ylabel("Scores")
plt.plot()
plt.savefig("Homework_Score_Distributions.png", dpi=100)
plt.show()



