# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:42:23 2020

@author: s-pc
"""
import keras
from keras.datasets import mnist
import matplotlib
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
import numpy as np
from keras.utils import to_categorical