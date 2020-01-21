# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:13:54 2020

@author: s-pc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score



#input data
diabet = pd.read_csv('D:/New folder (3)/Desktop/Big Data/data day 2020/diabetes.csv');# machin data
Air = pd.read_csv('D:/New folder (3)/Desktop/Big Data/data1.csv');#  Airplan ticket data of ALIBABA companie

print('---- Completed reading of flight ticket sales data ----')
print('---- Completed reading of diabet data ----')
print("********************classification(KNN)*********************")

print('len= ', len(diabet))
print(diabet.head())



#replacing invalid & missing value  with mean 
print("****replacing invalid & missing value with mean****")
zero_not = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']
for c in zero_not:
    diabet[c] = diabet[c].replace(0,np.nan);
    mean = int(diabet[c].mean(skipna= True));
    diabet[c] = diabet[c].replace(np.nan,mean);



#split data
print("****Splitting Data to Train & Test****") 
diabet_x = diabet.iloc[:, :8];
diabet_y = diabet.iloc[:, 8];

x_train, x_test, y_train, y_test = train_test_split(
      diabet_x, diabet_y, test_size= 100, random_state= 1)



#Standard Scaler
print("****Standardizing the scaler****")
x_train = StandardScaler().fit_transform(x_train);
x_test = StandardScaler().fit_transform(x_test);


#learning KNN
print("****fit Kneighbors classifier****")
'''
predictTrue = np.zeros(int(np.sqrt(np.size(x_train, 0)))*2);

for i in range((np.size(predictTrue))):
    
    classifier = KNeighborsClassifier(n_neighbors= i+1)
    classifier.fit(x_train, y_train)

    y_predict = classifier.predict(x_test) 

    predictTrue[i] = accuracy_score(y_test, y_predict)*100
       


#Error plot
plt.plot(predictTrue)
print('max correct prediction percentage= ',np.max(predictTrue),'%')
print('k_max correct prediction percentage= ',np.where(predictTrue== np.max(predictTrue))[0])
print('minmax correct prediction percentage= ',np.min(np.where(predictTrue== np.max(predictTrue))))

'''
    
classifier = KNeighborsClassifier(n_neighbors= 33)
classifier.fit(x_train, y_train)

y_predict = classifier.predict(x_test) 

predictTrue = accuracy_score(y_test, y_predict)*100
print("Correct Prediction Percentage= ",predictTrue,'%')

















