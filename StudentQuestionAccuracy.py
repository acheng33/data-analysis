from dotenv import load_dotenv
import pymongo
import os
from collections import Counter
import matplotlib.pyplot as plt

# Loading environment variables
load_dotenv(dotenv_path=".env")
database_url = os.environ.get("CS125MONGO")

# Connecting to the database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

# A list of every collection present
field_pl_submissions = db.plSubmissions

def StudentQuestionAccuracy():
    counter = 1
    counts_score = Counter()
    #Find every submission for each question per person
    for document in field_pl_submissions.find():
        print(counter)
        counter += 1
        if "email" in document:
            email = document['email']
        if "question_name" in document:
            question = document['question_name']

        if (email not in counts_score):
            counts_score[email] = Counter()
            counts_score[email][question] = False

        score = document['score']
        #Done to avoid repeating multiple successful submissions
        if (score is not None and score > 0 and question not in counts_score[email]):
            counts_score[email][question] = True

    fractions_score = Counter()

    for email in counts_score:
        for question, positive_score in counts_score[email].items():
            if question not in fractions_score:
                fractions_score[question] = Counter()
                fractions_score[question]["Numerator"] = 0
                fractions_score[question]["Denominator"] = 0

            fractions_score[question]["Denominator"] += 1

            if (positive_score):
                fractions_score[question]["Numerator"] += 1
    return fractions_score

scores = StudentQuestionAccuracy()

x = []
y = []

for question in scores:
    x.append(question)
    numerator = scores[question]["Numerator"]
    denominator = scores[question]["Denominator"]
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
plt.xticks(x, x, rotation=90)

plt.title("Percentage Of Students Who Got More Than 0 Points")
plt.xlabel("Questions")
plt.ylabel("Percentages")
plt.plot()
plt.savefig("Student_Question_Accuracy.png")
plt.show()
