# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:42:23 2020

@author: s-pc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import variance_threshold



x, y = fetch_covtype(data_home='./covtype_data/', return_X_y= True)
