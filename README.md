# data-analysis
CS 125 Course Development

## Setup
In order to set up your environment properly, you will need a `.env` file which should include any environment variables that will need to be used in the files of code. 

## Dependencies
- `collections`
- `dotenv`
- `json`
- `matplotlib`
- `numpy`
- `os`
- `pandas`
- `pickle`
- `pprint`
- `pymongo`
- `seaborn`
- `sklearn`
- `statistics`
- `sys`

## File Descriptions

#### AverageHomeworkScore.py
This program will generate a graph displaying the mean score per homework assignment for Fall 2019. Changing the db variable's client should enable other semesters' data to be plotted. 

#### AverageLabScore.py
This program will generate a graph displaying the mean score per lab assignment for Fall 2019. Changing the db variable's client should enable other semesters' data to be plotted. 

#### AverageNumberAttempts.py
Generates png images that house bargraphs of average number of tries on a question to the name of the question along with the version if applicable. Average number of tries has been listed above each bar to help with clarity. 

#### CreateDictionary.py
Creates a nested dictionary for use in other files. Dictionary formatted as such:
```
{student_email: {question_id: {timestamp : score}}}
```

#### exam_state.py
This piece of code will print out the percentages of students getting 0, 0~100, 100 respectively in each of the 12 quizzes. An example pie chart will be shown at the end of the execution. (also included in the repo)

#### matrix.py
This piece of code will save the data containing students' final hw, lecture, lab, mp, exam, quiz scores in a csv file called `student_scores.csv`
generate a graph displaying the mean score per lab assignment for Fall 2019. Changing the db variable's client should enable other semesters' data to be plotted. 

#### PrintJson.py
Prints the document structure of the first document in each collection within a given database into a text file. Each collection name is untabbed with the first layer of the document structure having one tab and each subsequent layer using more tabs. There is a line of white space between collections for identification and ease of reading. For example:
```
collection name
    first object
        values within first object
    second object
    
second collection name
```

#### regression.py
This piece of code performs linear regression using students' final hw, lecture, lab, mp, exam scores as inputs and quiz scores as target. It prints out the first five lines of (actual, predicted) pairs that are generated using the validation set as well as various error indices. In terms of RMSE (< 10% mean), this prediction using a linear model is mediocre but usable. Example outputs are shown below. 
- User Input
    - User will be prompted to type in a string in the format of hw, lecture, lab, mp, exam, quiz (in decimal numbers, representing scores for each category) and press Enter to get the result of predicted quiz score based upon the user input. 

- Output Description
| index | Actual | Predicted |
| ----- | ------ | --------- |
|0      | 85.00  | 85.418596 | 
|1      | 82.75  | 83.020833 | 
|2      | 89.83  | 91.892640 | 
|3      | 90.58  | 85.841761 | 
|4      | 89.75  | 90.129976 | 

Mean Absolute Error: 4.528901230422532 <br />
Mean Squared Error: 36.374491435244245 <br />
Root Mean Squared Error: 6.031126879385331 <br />
R Square Error is: 0.9599569544520193

#### SubmissionAccuracy.py 
This program will generate a graph containing the number of submissions that got a score greater than 0 per homework assignment, lab, quiz and midterm. Each student can have multiple submissions.

#### StudentQuestionAccuracy.py
This program will generate a graph containing the number of students that got a final score greater than 0 for every question in the homework, labs and quizzes. It requires 2 arguments. The first argument must be the year and semester of the client, in the format "year_semester". For example, Fall 2019 would be passed as "2019_Fall". The second argument is the specific homework, lab or quiz for which the graph is required. For example, entering "Q6" would generate the graph containing every question and the data from quiz 6. 