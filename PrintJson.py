from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

database_url = os.environ.get("CS125MONGO")
print(database_url)

client = MongoClient(database_url)
db = client.Fall2019Clean

collection = db.plSubmissions

first_document = collection.find_one()

print(first_document)