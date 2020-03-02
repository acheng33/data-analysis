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

#appending to collection name list all collections
#information over the course of the semester
collection_names.append(db.best)
collection_names.append(db.bestChanges)
collection_names.append(db.bestStats)

#information from discourse
collection_names.append(db.discourseUsers)
collection_names.append(db.discourseUserChanges)

plSubmissions_collection = db.jeed

first_document = plSubmissions_collection.find_one()


def print_json_keys(collection):
    first_document = collection.find_one()
    
    for key in first_document:
        print(key)
        if isinstance(first_document[key], dict) or isinstance(first_document[key], list):

            for second_key in first_document[key]:
                print("\t" + second_key)
                if (isinstance(first_document[key][second_key], dict) or isinstance(first_document[key][second_key], list)):

                    for third_key in first_document[key][second_key]:
                        print("\t\t" + third_key)

# for field in first_document:
#     print(field)

print_json_keys(plSubmissions_collection)