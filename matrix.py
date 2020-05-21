
import pymongo
import os
import json
import pprint
import pickle
import numpy as np
import pandas as pd    


import matplotlib.pyplot as plt

from dotenv import load_dotenv
# load our link 
load_dotenv()
database_url = os.environ.get("CS125MONGO")

# connect to the mongo database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

list_ = list()
# number of students 
student_number = 0
for instance in db['best'].find():
    l_ = list()
    hw = instance['homework']['totals']['noDrops']['percent']
    lecture = instance['lectures']['totals']['noDrops']['percent']
    quiz = instance['quizzes']['totals']['noDrops']['percent']
    lab = instance['labs']['totals']['noDrops']['percent']
    mp = instance['MPs']['totals']['noDrops']['percent']
    exam = instance['exams']['totals']['noDrops']['percent']
    l_ = [student_number, hw, lecture, lab, mp, exam, quiz]
    flag = (hw <= 10) and (lecture <= 10) and (quiz <= 10) and (lab <= 10) and (mp <= 10) and (exam <= 10)
    if (not flag):
        list_.append(l_)
        student_number += 1
# pprint.pprint(instance)


df = pd.DataFrame(list_)
df.columns = ['student_number', 'hw', 'lecture', 'lab', 'mp', 'exam', 'quiz']
df.to_csv('student_scores.csv', index=False)

for i in range(0,100):
    print(list_[i])
