import pymongo
import os
import json

from dotenv import load_dotenv

#loads environment variables and connects to database
load_dotenv()
database_url = os.environ.get("CS125MONGO")
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

if (db):
    print("success")