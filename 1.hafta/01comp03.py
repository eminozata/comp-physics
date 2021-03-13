import numpy as np
import matplotlib.pyplot as plt

vp_initial = 0.0
N = 3000
vvp = np.zeros(N)
vt = np.linspace(0.0, 5., N)
h = vt[1] - vt[0]
vxp = np.zeros(N)
vxp[0] = 0.0
vvp[0] = vp_initial

for k in range(1, N):
    vvp[k] = vvp[k-1] + h * (1. - vvp[k-1] ** 2)
    vxp[k] = vxp[k-1] + h * vvp[k-1]
A
plt.plot(vt, vvp, vt, np.tanh(vt), vt, np.abs(vvp- np.tanh(vt))*1000.)
plt.ylabel("$v/v_0$")
plt.xlabel("$t g/v_0$")
plt.show()
