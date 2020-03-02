from pymongo import MongoClient
from dotenv import load_dotenv

import os
import json

#load in environment variables
load_dotenv()
database_url = os.environ.get("CS125MONGO")

#connect to the mongo database
client = MongoClient(database_url)
db = client.Fall2019Clean

#list of collection names
collection_names = []

# appending to collection name list all collections
# information over the course of the semester
collection_names.append(db.best)
collection_names.append(db.bestChanges)
collection_names.append(db.bestStats)

#information from discourse
collection_names.append(db.discourseUsers)
collection_names.append(db.discourseUserChanges)

#information about lab, enrollment, and the class
collection_names.append(db.enrollment)
collection_names.append(db.labAttendance)
collection_names.append(db.people)
collection_names.append(db.peopleChanges)
collection_names.append(db.state)

#information about lecture
collection_names.append(db.lectureAttendance)
collection_names.append(db.lectureSummary)
collection_names.append(db.sliderChanges)
collection_names.append(db.jeed)

#information about MPs
collection_names.append(db.MPGrades)
collection_names.append(db.gradlegrader)
collection_names.append(db.intellijlogger)

#information about PairieLearn
collection_names.append(db.plAssessments)
collection_names.append(db.plGrades)
collection_names.append(db.plInstances)
collection_names.append(db.plQuestions)
collection_names.append(db.plSubmissions)

file = open("JSONKeys.txt", "w")

def print_json_keys_to_file(collection):
    file.write(collection.name)
    first_document = collection.find_one()
    
    for key in first_document:
        file.write("\n\t" + key)
        if isinstance(first_document[key], dict):

            for second_key in first_document[key]:
                file.write("\n\t\t" + second_key)
                if isinstance(first_document[key][second_key], dict):
                    
                    for third_key in first_document[key][second_key]:
                        file.write("\n\t\t\t" + third_key)

    file.write("\n\n")

for collection in collection_names:
    print_json_keys_to_file(collection)

file.close()