import pymongo
import os
import json
import pprint
import pickle
import numpy as np
import pandas as pd    
import numpy.linalg as la

import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# from dotenv import load_dotenv
# # load our link 
# load_dotenv()
# database_url = os.environ.get("CS125MONGO")

# # connect to the mongo database
# client = pymongo.MongoClient(database_url)
# db = client.Fall2019Clean

df = pd.read_csv('student_scores.csv')


###################################-----------LINEAR REGRESSION MODEL BY CLASSIC MATRIX MANIPULATION------------------############
# matrix = df.iloc[1:, 1:].to_numpy()
# A = matrix[:, 0:-1]
# b = matrix[:, -1]

# # append a column of ones
# ones = np.ones((len(b), 1))
# matrix = np.hstack((ones, matrix))
# print(matrix)
# A = matrix[:, 0:-1]

# # define training set and test set
# training_A = A[0:639, :]
# training_b = b[:639]

# test_A = A[639:, :]
# test_b = b[639:]

# # regular solution by AT A x = AT b
# learn_mat = la.solve(training_A.T.dot(training_A), training_A.T.dot(training_b))

# y_pred = list()
# for i in range(len(test_b)):
#     test_ = test_A[i, :]
#     predicted = test_@learn_mat
#     y_pred.append(predicted)
#     expected = test_b[i]
#     print("predicted is :" + str(predicted))
#     print("expected is :" + str(expected))
#     print("error is :" + str(abs(predicted - expected) / expected))

# y_pred = np.array(y_pred)

# print('R Square Error is:', r2_score(test_b, y_pred))
# print(learn_mat)



########################################------USING SCIKIT LEARN----------#############################################
A = df[['hw', 'lecture', 'lab', 'mp', 'exam']].values
b = df['quiz'].values


X_train, X_test, y_train, y_test = train_test_split(A, b, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm

# To retrieve the intercept:
intercept = regressor.intercept_
# For retrieving the slope:
learning_mat = regressor.coef_

# Predicted value by test
y_pred = regressor.predict(X_test)
# Save (actual, predicted) pairs in a pd data frame
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df.head(5))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R Square Error is:', r2_score(y_test, y_pred))

import sys

# function for transform input string to output quiz score
def predict(s):
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    s = s.split(",")
    if (len(s) != 5): 
        return "please enter 5 elements"
    s = np.array(s).astype(np.float32)
    for i in s:
        if (i > 100 or i < 0): return "please enter only elements w/ value (0,100)"
    s = s.reshape(1, -1)
    result = regressor.predict(s)
    return result

print("\n")
print("Please enter params in the following sequence: hw, lecture, lab, mp, exam. Separated by commas, one line at a time. Type quit to exit")
for line in sys.stdin:
    if (line == "quit\n"): 
        break
    print("Result quiz socore is: ", predict(line), "enter another line or type quit to exit")


# # Can show a plot for DF if needed
# df.plot(kind='bar',figsize=(10,8))
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()

