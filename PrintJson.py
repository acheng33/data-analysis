from pymongo import MongoClient
from dotenv import load_dotenv

import os
import json
import pprint

load_dotenv()

database_url = os.environ.get("CS125MONGO")

client = MongoClient(database_url)
db = client.Fall2019Clean

plSubmissions_collection = db.plSubmissions

first_document = plSubmissions_collection.find_one()

for field in first_document:
    print(field)