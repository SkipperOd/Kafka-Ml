import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("Salary_Data.csv")

#Separate Feature and Traget matrixs
x = data.iloc[:,:-1].values
y = data.iloc[:,1].values

#Split the train and test dataset
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = .9)

#Define the Machine Learning Alorithm
ml = LinearRegression()

#Train the Machine Learning Algorithm (Learning)
ml.fit(x_train,y_train)

#Test the Machine Learning Algorithm (Prediction)
y_pred = ml.predict(x_test)
print(x_test)
test_pred_x = [[15.5]]
test_pred_y = ml.predict(test_pred_x)
plt.scatter(x_test,y_test,color= 'red')
plt.plot(x_test,y_pred,color='blue')
plt.scatter(test_pred_x,test_pred_y,color='green')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.show()

print(ml.score(x_test,y_test))
