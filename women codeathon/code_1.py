import pandas as pd
import numpy as np
import matplotlib.pyplot as inline
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

''' Load the dataset'''

#data = pd.read_excel('C:\Users\sange\Desktop\learning\women codeathon\DM marks.xlsx')

data = pd.read_excel('DM marks.xlsx', sheet_name='Sheet1')



'''Split the dataset into training and testing sets'''
X = data.iloc[:, 1:-1]
y = data.iloc[:, -1]
#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


'''Create a linear regression model and fit it on the training data'''
model = LinearRegression()
model.fit(X_train, y_train)

'''https://realpython.com/train-test-split-python-data/
 same value coming for .score()'''
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

'''Make predictions on the testing data'''
y_pred = model.predict(X_test)
print(y_pred)



'''Evaluate the model using mean squared error'''
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)