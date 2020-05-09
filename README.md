# data-analysis
CS 125 Course Development

## Setup
In order to set up your environment properly, you will need a `.env` file which should include any environment variables that will need to be used in the files of code. 
Ensure that `pymongo` and `json` have been downloaded locally before trying to run to ensure correct results. 

## File Descriptions
#### PrintJson.py
Prints the document structure of the first document in each collection within a given database into a text file. Each collection name is untabbed with the first layer of the document structure having one tab and each subsequent layer using more tabs. There is a line of white space between collections for identification and ease of reading. For example:
```
collection name
    first object
        values within first object
    second object
    
second collection name
```
To run, run `python3 PrintJson.py`. 


# state-students-endup-in-quiz
CS 125 Course Development

## Setup
In order to set up your environment properly, you will need a `.env` file which should include any environment variables that will need to be used in the files of code. 
Ensure that `pymongo` and `json` have been downloaded locally before trying to run to ensure correct results. 

## File Descriptions
#### exam_state.py
To run, run `python3 exam_state.py`. 
This piece of code will print out the percentages of students getting 0, 0~100, 100 respectively in each of the 12 quizzes. An example pie chart will be shown at the end of the execution. (also included in the repo)

