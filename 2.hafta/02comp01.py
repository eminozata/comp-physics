import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi

def f(t, v):
    result = np.zeros(2, dtype=float)
    result[0] = v[1]
    result[1] = -sin(v[0])
    return result

amplitude = pi/1.2
t_initial = 0.0
t_final = 10.
vt = np.linspace(t_initial, t_final, 5000)
h = vt[1] - vt[0]
v_initial = np.array([amplitude, 0.])
vtheta_linear = amplitude * np.cos(vt)
vtheta_nolinear = np.zeros(vt.size, dtype=float)

v = np.array(v_initial)
vtheta_nolinear[0] = amplitude

for k in range(vt.size-1):
    v = v + h*f(vt[k], v)
    vtheta_nolinear[k+1] = v[0]


plt.plot(vt,vtheta_nolinear, vt, vtheta_linear)
plt.show()
