from dotenv import load_dotenv
import pymongo
import os
from collections import Counter
import matplotlib.pyplot as plt
import sys
import json

# Loading environment variables
load_dotenv(dotenv_path=".env")
database_url = os.environ.get("CS125MONGO")

# Connecting to the database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

# A list of every collection present
field_pl_submissions = db.plSubmissions

def StudentQuestionAccuracy():
    counts_score = Counter()
    #Find every submission for each question per person
    for document in field_pl_submissions.find():
        if "email" in document and "question_name" in document:
            email = document['email']
            question = document['question_name']
        else:
            continue
        #Adds a key email to a value counter. This counter has a key question and a default value of false.
        if (email not in counts_score):
            counts_score[email] = Counter()

        if (question not in counts_score[email]):
            counts_score[email][question] = False

        score = document['score']
        #Done to avoid repeating multiple successful submissions
        if (score is not None and score > 0 and counts_score[email][question] == False):
            counts_score[email][question] = True

    fractions_score = Counter()

    for email in counts_score:
        for question, is_positive_score in counts_score[email].items():
            #Adds the question key to the counter.
            if question not in fractions_score:
                fractions_score[question] = Counter()
                fractions_score[question]["Numerator"] = 0
                fractions_score[question]["Denominator"] = 0

            fractions_score[question]["Denominator"] += 1

            if (is_positive_score):
                fractions_score[question]["Numerator"] += 1

    return fractions_score

scores = StudentQuestionAccuracy()
with open("StudentProbabilities.json", "w") as file:
    json.dump(scores, file)

def PlotChosenAssignment():
    with open("StudentProbabilities.json", "r") as file:
        data = json.load(file)
    year = sys.argv[1]
    selected_assignment = sys.argv[2]
    selected_assignment = year + "_" + selected_assignment

    x = []
    y = []

    for question in data:
        if selected_assignment in question:
            name = question.replace(selected_assignment, "")
            name = name.replace("_", "")
            x.append(name)
            numerator = data[question]["Numerator"]
            denominator = data[question]["Denominator"]
            y.append((numerator / denominator) * 100)

    colors = {1 : 'darkgreen', 2 : 'royalblue'}
    bar_colors = []
    is_green_bar = True

    for value in x:
        if is_green_bar:
            bar_colors.append(1)
            is_green_bar = False
        else:
            bar_colors.append(2)
            is_green_bar = True

    bars = plt.bar(x, y, edgecolor='black', color=[colors[elem] for elem in bar_colors])

    plt.xticks(x, x, rotation=45)
    plt.title("Percentage Of Students Who Got More Than 0 Points in each question")
    plt.xlabel(selected_assignment)
    plt.ylabel("Percentages")
    plt.plot()
    plt.savefig("Student_Question_Accuracy.png")
    plt.show()

PlotChosenAssignment()