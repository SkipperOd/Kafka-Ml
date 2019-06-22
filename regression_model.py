import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

split_size = .8
class model():
    def data_pre_processing(self):
        data = pd.read_csv("model_data/data.csv")
        x = data.iloc[:,:-1].values
        y = data.iloc[:,1].values
        return train_test_split(x,y,test_size = split_size)

    def training(self,training_data):
        model = LinearRegression()
        print(training_data)
        model.fit(training_data["x_train"],training_data["y_train"])
        return model

    def visualization(self):
        plt.close('all')
        y_pred = self.model_data["model"].predict(self.model_data["testing_data"]["x_test"])
        plt.scatter(self.model_data["testing_data"]["x_test"],self.model_data["testing_data"]["y_test"],color= 'red')
        plt.plot(self.model_data["testing_data"]["x_test"],y_pred,color='blue')
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        
        plt.show()
        print(self.model_data["model"].score(self.model_data["testing_data"]["x_test"],self.model_data["testing_data"]["y_test"]))

        self.save()

    def predict(self,pred_x):
        
        pred_x = [[pred_x]]
        pred_y = self.model_data["model"].predict(pred_x)
        y_pred = self.model_data["model"].predict(self.model_data["testing_data"]["x_test"])
        plt.scatter(self.model_data["testing_data"]["x_test"],self.model_data["testing_data"]["y_test"],color= 'red')
        plt.plot(self.model_data["testing_data"]["x_test"],y_pred,color='blue')
        plt.scatter(pred_x,pred_y,color='green')
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        print("predicted value : ",pred_y)
        plt.show()
    
    def save(self):
        joblib.dump(self.model_data["model"], 'model/model.pkl') 

    def load(self):
        return joblib.load('model/model.pkl') 

    def __init__(self):
        x_train,x_test,y_train,y_test = self.data_pre_processing()
        training_data = {
            "x_train" :x_train ,
            "y_train" : y_train
        }
        testing_data = {
            "x_test" : x_test,
            "y_test" : y_test
        }
        model = self.training(training_data)
        self.model_data= {
            "model" : model,
            "testing_data" : testing_data,
            "training_data" :training_data
        }
        self.visualization()

    def update(self):
        x_train,x_test,y_train,y_test = self.data_pre_processing()
        training_data = {
            "x_train" :x_train ,
            "y_train" : y_train
        }
        testing_data = {
            "x_test" : x_test,
            "y_test" : y_test
        }
        model = self.training(training_data)
        self.model_data= {
            "model" : model,
            "testing_data" : testing_data,
            "training_data" :training_data
        }
        self.visualization()
    
    













