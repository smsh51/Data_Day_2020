# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from mpl_toolkits import mplot3d
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



#input Data
x, y = load_breast_cancer(True)


#Standartdization
x = scale(x)

#spitting train & test data
x_train, x_test, y_train, y_test = train_test_split(x, y,
            test_size= 100, random_state= 1)


c = ['rbf', 'linear', 'poly', 'sigmoid']
#fiting algorithm SVC
for i in c:
    for j in range(50):
        model = SVC(C= j+1, kernel= i)
        model.fit(x_train, y_train)


#prediction
        y_predict = model.predict(x_test)


#accuracy
        print('cpp',i,'&',j,'=',accuracy_score(y_test,y_predict)*100,'%')
