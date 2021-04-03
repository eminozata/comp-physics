# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:38:30 2021

@author: Asus
"""


import numpy as np
import matplotlib.pyplot as plt
def integrator(f,method,t_initial,t_final,x_initial,N):
    vt=np.linspace(t_initial,t_final,N)
    X=np.zeros((N,x_initial.size),dtype=type(x_initial))
    X[0]=x_initial
    h=vt[1]-vt[0]
    for k in range(1,N):
        X[k]=method(f,vt[k-1],   X[k-1],h)
    return (vt,X)
   
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
#d^2/dt^2 x(t)=-x(t)    x[0] is position x[1]: velocity
def simple_pendulum(t,x):
    res=np.zeros(x.size,dtype=type(x[0]))# res=0.*x
    res[0]=x[1]
    res[1]=-x[0]
    return res
vt,X=integrator(simple_pendulum,euler,0.0,20.,np.array([1.0,0.]),2000)
vt,X_runga=integrator(simple_pendulum,runga_kutta2,0.0,20.,np.array([1.0,0.]),2000)
vt,X_runga4=integrator(simple_pendulum,runga_kutta4,0.0,20.,np.array([1.0,0.]),2000)
plt.plot(vt,X[:,0],vt,1.02*X_runga[:,0],'--',vt,np.cos(vt))

plt.show()
print((np.abs(X[:,0]-np.cos(vt))).max())    
print((np.abs(X_runga[:,0]-np.cos(vt))).max())
print((np.abs(X_runga4[:,0]-np.cos(vt))).max())
