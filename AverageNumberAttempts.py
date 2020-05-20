import pymongo
import os
import json
import matplotlib.pyplot as plt

from dotenv import load_dotenv
from CreateDictionary import create_dictionary

#Loads environment variables and connects to database
load_dotenv()
database_url = os.environ.get("CS125MONGO")
client = pymongo.MongoClient(database_url)
db = client.Fall2019Clean

#Creates dictionary for each student with timestamps of each submission of assignment
full_dictionary = create_dictionary()

#Sets up the collection which holds the id for each question in labs, homeworks, and exams
question_collection = db.plQuestions
question_list = list(question_collection.find().sort("ID", 1))

#Finds repeat question versions and removes them
questions_to_remove = []

for i in range(len(question_list)):
    question = question_list[i]
    if '125' in question_list[i]['ID']:
        questions_to_remove.append(question)

for question in questions_to_remove:
    question_list.remove(question)

#Calculates the average number of attempts a person takes for each question
def get_number_of_attempts():
    assignment_to_average_attempts = {}

    #Iterates through each question to get the id
    for i in range(len(question_list)):
        question_id = question_list[i]['ID']
        people_to_attempts = {}
        total_attempts = 0

        #For each question, associate people to number of tries they took 
        for person in full_dictionary:
            person_question_ids = list(full_dictionary[person].keys())

            for question in person_question_ids:
                if "125" in question:
                    new_question_id = question[0:13] + question[17:]
                    insert_into_dictionary = {new_question_id: full_dictionary[person][question]}
                    full_dictionary[person].update(insert_into_dictionary)
                    full_dictionary[person].pop(question)

            if question_id in person_question_ids:
                people_to_attempts.update({person : len(full_dictionary[person][question_id])})

        #Iterate through created dictionary to get the total number of attempts made by everyone
        for person in people_to_attempts:
            total_attempts += people_to_attempts[person]
        
        #Updates the assignment to average dictionary by dividing the total_attempts calculated above by the people who have attempted the question
        if len(people_to_attempts) == 0:
            assignment_to_average_attempts.update({question_id: 0})
        else:
            assignment_to_average_attempts.update({question_id: total_attempts / len(people_to_attempts)})
        
        #Clear the dictionary to have it clearn for the next question
        people_to_attempts.clear()

    return assignment_to_average_attempts

resulting_dictionary = get_number_of_attempts()

#Gets X and Y values for charts from the resulting dictionary created
x_values = list(resulting_dictionary.keys())
y_values = list(resulting_dictionary.values())

#Removes prefix of each question name
for i in range(len(x_values)):
    x_values[i] = x_values[i][10:]

#Lists for the x and y values of each corresponding type of question
exam_x_values = []
exam_y_values = []

homework_x_values = []
homework_y_values = []

lab_x_values = []
lab_y_values = []

quiz_zero_one_x_values = []
quiz_zero_one_y_values = []

quiz_two_three_x_values = []
quiz_two_three_y_values = []

quiz_four_five_x_values = []
quiz_four_five_y_values = []

quiz_six_seven_x_values = []
quiz_six_seven_y_values = []

quiz_eight_nine_x_values = []
quiz_eight_nine_y_values = []

quiz_ten_eleven_x_values = []
quiz_ten_eleven_y_values = []

#Sorts the average number of tries into 
for i in range(len(x_values)):
    if ('E0' in x_values[i]) or ('E1' in x_values[i]) or ('E2' in x_values[i]):
        exam_x_values.append(x_values[i])
        exam_y_values.append(y_values[i])

    elif 'HW' in x_values[i]:
        homework_x_values.append(x_values[i])
        homework_y_values.append(y_values[i])

    elif 'Lab' in x_values[i]:
        lab_x_values.append(x_values[i])
        lab_y_values.append(y_values[i])

    elif ('Q10' in x_values[i]) or ('Q11' in x_values[i]):
        quiz_ten_eleven_x_values.append(x_values[i])
        quiz_ten_eleven_y_values.append(y_values[i])

    elif ('Q0' in x_values[i]) or ('Q1' in x_values[i]):
        quiz_zero_one_x_values.append(x_values[i])
        quiz_zero_one_y_values.append(y_values[i])

    elif ('Q2' in x_values[i]) or ('Q3' in x_values[i]):
        quiz_two_three_x_values.append(x_values[i])
        quiz_two_three_y_values.append(y_values[i])

    elif ('Q4' in x_values[i]) or ('Q5' in x_values[i]):
        quiz_four_five_x_values.append(x_values[i])
        quiz_four_five_y_values.append(y_values[i])

    elif ('Q6' in x_values[i]) or ('Q7' in x_values[i]):
        quiz_six_seven_x_values.append(x_values[i])
        quiz_six_seven_y_values.append(y_values[i])

    elif ('Q8' in x_values[i]) or ('Q8' in x_values[i]):
        quiz_eight_nine_x_values.append(x_values[i])
        quiz_eight_nine_y_values.append(y_values[i])

#Creates bar chart for average number of exam tries
bars = plt.bar(exam_x_values, exam_y_values, edgecolor = 'black', color = 'violet')
plt.xticks(exam_x_values, exam_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

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
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

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
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

plt.title("Average Number of Attempts per Question (Labs)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Labs.png")
plt.clf()

#Creates bar chart for average number of quiz tries in Q0, Q1
bars = plt.bar(quiz_zero_one_x_values, quiz_zero_one_y_values, edgecolor = 'black', color = 'mediumspringgreen')
plt.xticks(quiz_zero_one_x_values, quiz_zero_one_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.1, round(average, 1), rotation = 90)

plt.title("Average Number of Attempts per Question (Quiz 0, 1)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Quizzes_0_1.png")
plt.clf()

#Creates bar chart for average number of quiz tries in Q2, Q3
bars = plt.bar(quiz_two_three_x_values, quiz_two_three_y_values, edgecolor = 'black', color = 'bisque')
plt.xticks(quiz_two_three_x_values, quiz_two_three_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

plt.title("Average Number of Attempts per Question (Quiz 2, 3)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Quizzes_2_3.png")
plt.clf()

#Creates bar chart for average number of quiz tries in Q4, Q5
bars = plt.bar(quiz_four_five_x_values, quiz_four_five_y_values, edgecolor = 'black', color = 'silver')
plt.xticks(quiz_four_five_x_values, quiz_four_five_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

plt.title("Average Number of Attempts per Question (Quiz 4, 5)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Quizzes_4_5.png")
plt.clf()

#Creates bar chart for average number of quiz tries in Q6, Q7
bars = plt.bar(quiz_six_seven_x_values, quiz_six_seven_y_values, edgecolor = 'black', color = 'lightcoral')
plt.xticks(quiz_six_seven_x_values, quiz_six_seven_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

plt.title("Average Number of Attempts per Question (Quiz 6, 7)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Quizzes_6_7.png")
plt.clf()

#Creates bar chart for average number of quiz tries in Q8, Q9
bars = plt.bar(quiz_eight_nine_x_values, quiz_eight_nine_y_values, edgecolor = 'black', color = 'sandybrown')
plt.xticks(quiz_eight_nine_x_values, quiz_eight_nine_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

plt.title("Average Number of Attempts per Question (Quiz 8, 9)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Quizzes_8_9.png")
plt.clf()

#Creates bar char for average number of quiz tries in Q10, Q11
bars = plt.bar(quiz_ten_eleven_x_values, quiz_ten_eleven_y_values, edgecolor = 'black', color = 'gold')
plt.xticks(quiz_ten_eleven_x_values, quiz_ten_eleven_x_values, rotation = 90)

figure = plt.gcf()
figure.set_size_inches(25, 25)

for bar in bars:
    average = bar.get_height()
    plt.text(bar.get_x(), average + 0.25, round(average, 1), rotation = 90)

plt.title("Average Number of Attempts per Question (Quiz 10, 11)")
plt.xlabel("Question")
plt.ylabel("Number of Tries")
plt.plot()

plt.savefig("Average_Attempts_Quizzes_10_11.png")
plt.clf()