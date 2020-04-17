import pymongo
import os
import json

from dotenv import load_dotenv

#loads environment variables and connects to database
load_dotenv()
database_url = os.environ.get("CS125MONGO")
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

submission_collection = db.plSubmissions

#creates a nested dictionary where each person contains a question id and number of timestamps corresponding to how many times they submitted that question
def create_dictionary():
    count = 0
    dictionary_of_people = {}

    #loop through all the documents in the collection
    for document in submission_collection.find():
        count += 1
        #loops through the fields in the document
        timestamp = None
        email = None
        question_id = None
        score = None

        #loops through the document to find relevant fields
        for key in document:
            if key == "feedback" and not document[key] == None:
                #loops through feedback object to find score and timestamp
                for feedback_key in document[key]:
                    if feedback_key == "end_time":
                        timestamp = document[key][feedback_key]
                        
                    if feedback_key == "results":
                        for result_key in document[key][feedback_key]:
                            if result_key == "score":
                                score = document[key][feedback_key][result_key]

            #sets question_id
            if key == "question_name":
                question_id = document[key]
            #sets email
            if key == "email":
                email = document[key]
                
    return dictionary_of_people

create_dictionary()