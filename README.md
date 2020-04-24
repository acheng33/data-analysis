# regression-for-quiz-scores
CS 125 Course Development

## Setup
In order to set up your environment properly, you will need a `.env` file which should include any environment variables that will need to be used in the files of code. 
Ensure that `pymongo` and `json` have been downloaded locally before trying to run to ensure correct results. 

## File Descriptions
#### matrix.py
To run, run `python3 matrix.py`. 
This piece of code will save the data containing students' final hw, lecture, lab, mp, exam, quiz scores in a csv file called `student_scores.csv`
#### regression.py
To run, run `python3 regression.py`. 
This piece of code performs linear regression using students' final hw, lecture, lab, mp, exam scores as inputs and quiz scores as target. It prints out the first five lines of (actual, predicted) pairs that are generated using the validation set as well as various error indices. In terms of RMSE (< 10% mean), this prediction using a linear model is mediocre but usable. Example outputs are shown below.


## Output Descriptions
| index | Actual | Predicted |
| ----- | ------ | --------- |
|0      | 85.00  | 85.418596 | 
|1      | 82.75  | 83.020833 | 
|2      | 89.83  | 91.892640 | 
|3      | 90.58  | 85.841761 | 
|4      | 89.75  | 90.129976 | 
-----------------------------
Mean Absolute Error: 4.528901230422532 <br />
Mean Squared Error: 36.374491435244245 <br />
Root Mean Squared Error: 6.031126879385331 <br />
R Square Error is: 0.9599569544520193

