
import pymongo
import os
import json
import pprint
import pickle
import numpy as np

import matplotlib.pyplot as plt

from dotenv import load_dotenv
# load our link 
load_dotenv()
database_url = os.environ.get("CS125MONGO")

# connect to the mongo database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

array = np.zeros([12, 3])


# number of students 
student_number = 0

for instances in db['best'].find():
    # quiz number
    quiz_number = 0
    for quiz in instances["quizzes"]:
        if (quiz != "totals"):
            score = instances["quizzes"][quiz]['score']
            # for debug:
            # pprint.pprint(score)

            if score == 0: 
                array[quiz_number][0] += 1
            elif score < 100:
                array[quiz_number][1] += 1
            elif score == 100:
                array[quiz_number][2] += 1
            quiz_number += 1

    student_number += 1

for i in range(0, 12):
    #print("Average Q{} Score of students is: " + str(float(score_0 / count)) + "\n" format(i))
    print("For quiz: " + str(i) + "-----------------------------------------------------------")
    print("Percentage of students getting 0 on quiz {} is: ".format(i) + str(float(array[i][0] / student_number)) + "\n")
    print("Percentage of students getting (0, 100) on quiz {} is: ".format(i) + str(float(array[i][1] / student_number)) + "\n")
    print("Percentage of students getting 100 on quiz {} is: ".format(i) + str(float(array[i][2] / student_number)) + "\n")

print("Number of students in total: " + str(student_number))

labels = ['Getting 0 on Quiz 1', 'Getting (0,100) on Quiz 1', 'Getting 100 on Quiz 1']
sizes = array[1, :] * 100
sizes.tolist()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# file = open("MyKeys.pkl", "wb")

# pickle.dump(db['best'].find_one(), file)

# #closes file
# file.close()
