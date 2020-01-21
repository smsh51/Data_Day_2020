# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:02:56 2020

@author: s-pc
"""

import pandas as pd

def Input(x):
    try:    
        str(x)
    except ValueError:
        print ('Value not suport')
        
    if x == 'Air':
        return pd.read_csv('D:/New folder (3)/Desktop/Big Data/data1.csv', na_values= ['na','null','nan','NAN','NULL','Null']);
    else:
        print('defind value')