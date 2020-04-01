import pymongo
import os
import json
import matplotlib.pyplot as plt

#connect to the mongo database
cluster = pymongo.MongoClient("mongodb://Fall2019CleanRead:VIK4I0rg3EYKxrpF5l57RSDx5b26GSdD@cs125-mongo-01.cs.illinois.edu,cs125-mongo-02.cs.illinois.edu,cs125-mongo-03.cs.illinois.edu/Fall2019Clean?replicaSet=cs125&ssl=true")
db = cluster.Fall2019Clean

#creates list of collection of prairieLearn grades
collection = db["plGrades"]

#get the first midterm posts
firstMid = collection.find({"name" : "E0"})

#get the second midterm posts
secondMid = collection.find({"name" : "E1"})

#get the third midterm posts
thirdMid = collection.find({"name" : "E2"})

#collect all first midterm scores
firstMidScore = []
for item in firstMid:
    firstMidScore.append(item["score"])

#collect all second midterm scores
secondMidScore = []
for item in secondMid:
    secondMidScore.append(item["score"])

#collect all third midterm scores
thirdMidScore = []
for item in thirdMid:
    thirdMidScore.append(item["score"])

#plot the graph for the first midterm score distribution
colors = ['skyblue', 'tan', 'green']
legend = ['midterm1', 'midterm2', "midterm3"]
plt.hist([firstMidScore, secondMidScore, thirdMidScore], color = colors)
plt.title('score distribution of the midterms')
plt.xlabel("score")
plt.ylabel("number of students")
plt.legend(legend)
plt.savefig("mid1.png")
plt.show()
