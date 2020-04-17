import pymongo
import os
import json

from dotenv import load_dotenv

#loads environment variables and connects to database
load_dotenv()
database_url = os.environ.get("CS125MONGO")
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

#given an assignment number or assessment number, function will return the average number of tries per student for the question
#field in plQuestions: ID, field in plSubmissions: question_name
question_collection = db.plQuestions
submission_collection = db.plSubmissions


