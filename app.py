from pymongo import MongoClient
import os

from dotenv import load_dotenv

#load in environment variables
load_dotenv()
database_url = os.environ.get("CS125MONGO")

#connect to the mongo database
client = MongoClient(database_url)
db = client.Fall2019Clean