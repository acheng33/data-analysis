import pymongo
import os
import json
import matplotlib.pyplot as plt

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
    question_list = list(question_collection.find().sort("ID", 1))

    #iterates through each question to get the id
    for i in range(len(question_list)):
        question_id = question_list[i]['ID']
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
        if len(people_to_attempts) == 0:
            assignment_to_average_attempts.update({question_id: 0})
        else:
            assignment_to_average_attempts.update({question_id: total_attempts / len(people_to_attempts)})
        
        #clear the dictionary to have it clearn for the next question
        people_to_attempts.clear()

    return assignment_to_average_attempts

resulting_dictionary = get_number_of_attempts()

#Should merge all the exam, labs, homeworks from different versions into one coherent name
x_values = list(resulting_dictionary.keys())
y_values = list(resulting_dictionary.values())

exam_x_values = []
exam_y_values = []

homework_x_values = []
homework_y_values = []

lab_x_values = []
lab_y_values = []

quiz_x_values = []
quiz_y_values = []

for value in range(len(x_values)):
    if ('E0' in x_values[value]) or ('E1' in x_values[value]) or ('E2' in x_values[value]):
        exam_x_values.append(x_values[value][10:])
        exam_y_values.append(y_values[value])
    elif 'HW' in x_values[value]:
        homework_x_values.append(x_values[value][10:])
        homework_y_values.append(y_values[value])
    elif 'Lab' in x_values[value]:
        lab_x_values.append(x_values[value][10:])
        lab_y_values.append(y_values[value])
    elif 'Q' in x_values[value]:
        quiz_x_values.append(x_values[value][10:])
        quiz_y_values.append(y_values[value])

#Creates bar chart for average number of exam tries
bars = plt.bar(exam_x_values, exam_y_values, edgecolor = 'black', color = 'violet')
plt.xticks(exam_x_values, exam_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(18, 14)

plt.title("Average Number of Attempts per Question (Midterm)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Exam.png")
plt.clf()

#Creates bar chart for average number of homework tries
bars = plt.bar(homework_x_values, homework_y_values, edgecolor = 'black', color = 'mediumslateblue')
plt.xticks(homework_x_values, homework_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(18, 14)

plt.title("Average Number of Attempts per Question (Homework)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Homework.png")
plt.clf()

#Creates bar chart for average number of lab tries
bars = plt.bar(lab_x_values, lab_y_values, edgecolor = 'black', color = 'lightskyblue')
plt.xticks(lab_x_values, lab_x_values, rotation = 90)

figure = plt.gcf()

plt.title("Average Number of Attempts per Question (Labs)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Labs.png")
plt.clf()

#Creates bar chart for average number of quiz tries
bars = plt.bar(quiz_x_values, quiz_y_values, edgecolor = 'black', color = 'mediumspringgreen')
plt.xticks(quiz_x_values, quiz_x_values, rotation = 90)

figure = plt.gcf()

plt.title("Average Number of Attempts per Question (Quiz)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Quizzes.png")
plt.clf()