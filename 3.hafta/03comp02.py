# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:38:30 2021

@author: Asus
"""


import numpy as np
from math import sin,sqrt,cos,pi
import matplotlib.pyplot as plt
from time import time
def my_sinh(vt):
    sinh_=np.sinh(vt)
    large=sinh_>2.*pi
    sinh_[large]=2.*pi
    return sinh_
def integrator(f,method,t_initial,t_final,x_initial,N):
    vt=np.linspace(t_initial,t_final,N)
    X=np.zeros((N,x_initial.size),dtype=type(x_initial))
    X[0]=x_initial
    h=vt[1]-vt[0]
    for k in range(1,N):
        X[k]=method(f,vt[k-1],   X[k-1],h)
    return (vt,X)
def nolinear_pendulum(t,x):
    res=np.zeros(x.size,dtype=type(x[0]))# res=0.*x
    res[0]=x[1]
    res[1]=-sin(x[0])
    return res
def Jacobian(t,x):
    J=np.zeros((x.size,x.size),dtype=float)
    J[0,1]=1.0
    J[1,0]=-cos(x[0])
    return J
def runga_kutta2(f,t,x,h):
    kappa=0.5*h*f(t,x)
    return x+h*f(t+0.5*h,x+kappa)
def runga_kutta4(f,t,x,h):
    k1=h*f(t,x)
    k2=h*f(t+0.5*h,x+0.5*k1)
    k3=h*f(t+0.5*h,x+0.5*k2)
    k4=h*f(t+h,x+k3)
    return x+1./6*(k1+2*k2+2*k3+k4)
def euler(f,t,x,h):
    return x+h*f(t,x)
def simple_pendulum(t,x):
    res=np.zeros(x.size,dtype=type(x[0]))
    res[0]=x[1]
    res[1]=-x[0]
    return res
t_initial = 0.
t_final = 20.
x_initial = np.array([pi,0.001])
t1=time()

vt, X = integrator(nolinear_pendulum, runga_kutta4, 0.0, 20., np.array([1., 0., 0.]), 4000)
t2 = time()
t_runga_kutta = t2-t1

plt.plot(vt,X[:,0]%(2*pi),vt,X[:,1])
plt.show()
