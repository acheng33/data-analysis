from dotenv import load_dotenv
import pymongo
import os
from collections import Counter
import matplotlib.pyplot as plt
import sys

# Loading environment variables
load_dotenv()
database_url = os.environ.get("CS125MONGO")

# Connecting to the database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

# A list of every collection present
field_pl_submissions = db.plSubmissions

def SubmissionAccuracy():
    counts_score = Counter()
    fractions_score = Counter()

    #Total submissions
    number_of_records = 0
    #Submissions with a score greater than 0
    number_of_positive_scores = 0

    counter = 0
    for document in field_pl_submissions.find():
        print(counter)
        counter += 1
        current_assessment = document['assessment_name']
        score = document['score']

        #Gets the submission counts in case the name of the assessment changes due to a lack of ordering
        if number_of_records != 0 and current_assessment in counts_score:
            number_of_positive_scores = counts_score[current_assessment]['Numerator']
            number_of_records = counts_score[current_assessment]['Denominator']

        #Resets the total submissions and positive scores for a new assessment
        elif number_of_records != 0 and current_assessment not in counts_score:
            number_of_records = 0
            number_of_positive_scores = 0

        if number_of_records == 0:
            counts_score[current_assessment] = Counter()
            counts_score[current_assessment]['Numerator'] = number_of_positive_scores
            counts_score[current_assessment]['Denominator'] = number_of_records

        number_of_records += 1

        if score != None and score > 0:
            number_of_positive_scores += 1

        counts_score[current_assessment]['Numerator'] = number_of_positive_scores
        counts_score[current_assessment]['Denominator'] = number_of_records
        fractions_score[current_assessment] = number_of_positive_scores / number_of_records

    return fractions_score

scores = SubmissionAccuracy()

x = []
y = []

for assessment in scores:
    x.append(assessment)
    y.append(scores[assessment] * 100)

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

figure = plt.gcf()
figure.set_size_inches(18, 14)

plt.title("Percentage of submissions that got more than 0 points")
plt.xlabel("Question")
plt.ylabel("Percentage")
plt.plot()
plt.savefig("Submission_Accuracy.png")
plt.show()
