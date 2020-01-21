# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:52:02 2020

@author: s-pc
"""

from numba import jit
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

n = 1000000000;

@jit(nopython=True)
def monte_carlo_pi(nsamples):
    j = 2;
    k = 2;
    for i in range(nsamples):
        j = (k*k);
        k = k+2;
        #print('j=',j,'k=',k,'n=',n)
        
    return  j, k




df = pd.read_csv('D:/New folder (3)/Desktop/Big Data/data day 2020/mpg.csv');


print(df.head());

plt.scatter( x= df['displ'], y= df['hwy'], c= df['cyl'],
            marker='o', alpha=0.2);
plt.title('plot of displ & hwy & color= cyl')
plt.xlabel('displ')
plt.ylabel('hwy')
plt.colorbar()
plt.show();


x = df['displ']; y = df['cyl']; z = df['hwy'];

x1 = np.array([df['displ']]).T ;
y1 = np.array([df['cyl']]).T;
z1 = np.array([df['hwy']]).T;




@jit(nopython=True)
def plot(fig,ax):
    #fig = plt.figure(figsize=[10,10])
    #ax = plt.axes(projection= '3d')
    ax.scatter3D(x1, y1, z1, y1)
    plt.xlabel('displ')
    plt.ylabel('cyl')
    plt.clabel('hwy')
    plt.show();



fig = plt.figure();
ax = plt.axes(projection= '3d');
plot(fig,ax)





    