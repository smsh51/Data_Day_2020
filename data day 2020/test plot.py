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


sns.set_style('darkgrid')

#input data
df = pd.read_csv('D:/New folder (3)/Desktop/Big Data/data day 2020/mpg.csv');# machin data
Air = pd.read_csv('D:/New folder (3)/Desktop/Big Data/data1.csv');#  Airplan ticket data of ALIBABA companie
mis = pd.read_csv('D:/New folder (3)/Desktop/Big Data/data day 2020/mising.csv')# mising data


"********************classification*********************"


