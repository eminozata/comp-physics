# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:08:19 2021

@author: muham
"""

from scipy.special import roots_hermite
import numpy as np
from math import exp
import matplotlib.pyplot as plt

(r,w) = roots_hermite(8)

def Lagrange(f,x,xdata):
    ydata = f(xdata)
    s = x*0.0
    for k0 in range(xdata.size):
        pr = 1.0
        for k1 in range(xdata.size):
            if(k1!=k0):
                pr = pr*(x-xdata[k1])/(xdata[k0]-xdata[k1])
        s=s+ydata[k0]*pr
    return s
    
vx = np.linspace(0.,1.,100)
vy=vx*0.
xdata = np.linspace(0.,1.,10)


vy = Lagrange(np.exp, vx, xdata)
plt.plot(vx,vy,vx,np.exp(vx))