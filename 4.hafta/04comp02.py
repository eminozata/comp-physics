# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:24:30 2021

@author: Asus
"""
import numpy as np
def simspson(a,b,N):
    vx=np.linspace(a,b,N)
    weight=np.zeros(vx.size,dtype=float)
    h=vx[1]-vx[0]
    weight[::2]=2.*h/3
    weight[1::2]=4.*h/3
    weight[0]=h/3
    weight[weight.size-1]=h/3
    return (vx,weight)
    
    
N=257
(vx,weight)=simspson(0., 1., N)
res=(np.exp(vx)*weight).sum()
print('res=',res,' ',np.exp(1.)-1.)