import pymongo
import os
import json

from dotenv import load_dotenv
from CreateDictionary import create_dictionary

#loads environment variables and connects to database
load_dotenv()
database_url = os.environ.get("CS125MONGO")
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

full_dictionary = create_dictionary()

#sets up the collection which holds the id for each question in labs, homeworks, and exams
question_collection = db.plQuestions

def get_number_of_attempts():
    assignment_to_average_attempts = {}

    #iterates through each question to get the id
    for question in question_collection:
        question_id = question['ID']
        people_to_attempts = {}
        total_attempts = 0

        #for each question, associate people to number of tries they took 
        for person in full_dictionary:
            if question_id in full_dictionary[person]:
                people_to_attempts.update({person : len(full_dictionary[person][question_id])})

        #iterate through created dictionary to get the total number of attempts made by everyone
        for person in people_to_attempts:
            total_attempts += people_to_attempts[person]
        
        #updates the assignment to average dictionary by dividing the total_attempts calculated above by the people who have attempted the question
        assignment_to_average_attempts.update({question_id: total_attempts / len(people_to_attempts)})
        
        #clear the dictionary to have it clearn for the next question
        people_to_attempts.clear()

get_number_of_attempts()
