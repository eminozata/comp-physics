import numpy as np
import matplotlib.pyplot as plt
# dv/ dt = (gamma/m) v(t) differential equation to integrate
# euler method
# v(t_{n+1}) = v(t_n) - h*(gamma/m) *v_n
# gamma/m = 1.0 sec ^{-1}
# v0 = 3.0 m/sec
# t_ini = 0 sec
# t_fin = 6.0 sec

t_ini = 0.
t_fin = 6.0
N = 3000
vt = np.linspace(t_ini, t_fin, N)
v0 = 3.0
velocities = np.zeros(vt.size, dtype=float)
analytical_velocities = v0*np.exp(-vt)

# analytical
velocities[0] = v0
h= vt[1] - vt[0]

for k in range(1, N):
    velocities[k] = velocities[k-1] - h * velocities[k-1]
    print("k: ",k, " ", velocities[k])

#plot analytical values
plt.plot(vt, analytical_velocities)

#plot our values
plt.plot(vt, velocities)
plt.show()
