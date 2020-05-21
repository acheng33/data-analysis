import pymongo
import os
import json

from dotenv import load_dotenv

#load in environment variables
load_dotenv(dotenv_path=".env")
database_url = os.environ.get("CS125MONGO")

#connect to the mongo database
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

#creates list of collection names and sorts
collection_names = db.list_collection_names()
collection_names.sort()

#opens the file to write json keys into
file = open("JSONKeys.txt", "w")

#function which takes in a list of names of collections and writes the keys of the json in each collection to a file
#param (collections) a list of names of collections which to find the json keys for
def print_json_keys_to_file(collections):
    #keeps track of the index of the current collection
    counter = 0
   
    #loops through all the collections
    for collection in collections:
        #finds collection from database
        current_collection = pymongo.collection.Collection(db, collections[counter], create = False)
        counter += 1
        
        #writes the name of collection to file
        file.write(current_collection.name)
        first_document = current_collection.find_one()
        
        #loops through the document and writes the json keys to previously specified file
        for key in first_document:
            file.write("\n\t" + key)
            if isinstance(first_document[key], dict):

                for second_key in first_document[key]:
                    file.write("\n\t\t" + second_key)
                    if isinstance(first_document[key][second_key], dict):
                        
                        for third_key in first_document[key][second_key]:
                            file.write("\n\t\t\t" + third_key)
                            if isinstance(first_document[key][second_key][third_key], dict):
                                
                                for fourth_key in first_document[key][second_key][third_key]:
                                    file.write("\n\t\t\t\t" + fourth_key)

        file.write("\n\n")

print_json_keys_to_file(collection_names)

#closes file
file.close()






# # sum of all quiz 0 scores
# score_ = 0
# # number of students getting 0 on quiz 0 
# score_0 = 0
# # number of students getting (0, 100) on quiz 0 
# score_less = 0
# # number of students getting 100 on quiz 0 
# score_0_100 = 0
# # number of students 


# import pymongo
# import os
# import json
# import pprint
# import pickle
# import numpy as np

# import matplotlib

# from dotenv import load_dotenv
# # load our link 
# load_dotenv()
# database_url = os.environ.get("CS125MONGO")

# # connect to the mongo database
# client = pymongo.MongoClient(database_url)
# db = client.Fall2019Clean

# array = np.zeros([12, 3])


# # number of students 
# student_number = 0

# for instances in db['best'].find():
#     # quiz number
#     quiz_number = 0
#     for quiz in instances["quizzes"]:

#         score = quiz['score']
#         if score == 0: 
#             array[quiz_number][0] += 1
#         elif score < 100:
#             array[quiz_number][1] += 1
#         elif score == 100:
#             array[quiz_number][2] += 1
#         quiz_number += 1
#     student_number += 1

# for i in range(0, 12):
#     #print("Average Q{} Score of students is: " + str(float(score_0 / count)) + "\n" format(i))
#     print("Number of students getting 0 on quiz {} is: " + str(float(array[i][0] / student_number)) + "\n" .format(i))
#     print("Number of students getting (0, 100) on quiz {} is: " + str(float(array[i][1] / student_number)) + "\n" .format(i))
#     print("Number of students getting 100 on quiz {} is: " + str(float(array[i][2] / student_number)) + "\n" .format(i))