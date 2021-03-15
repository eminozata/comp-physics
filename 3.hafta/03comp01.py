import numpy as np
import matplotlib.pyplot as plt

def integrator(f, method, t_ini, t_fin, x_ini, N):
    vt = np.linspace(t_ini, t_fin, N)
    X = np.zeros((N,x_ini.size), dtype = type(x_ini))
    X[0] = x_ini
    h = vt[1] - vt[0]
    for k in range(1,N):
        X[k] = method(f,vt[k-1], X[k-1] ,h)
    return (vt, X)


def runge_kutta2(f, t, x, h):
    kappa = 0.5 * h * f(t, x)
    return x + h * f(t + 0.5 * h, x + kappa)

def runge_kutta4(f, t, x, h):
    k1 = h * f(t,x)
    k2 = h * f(t + 0.5 * h, x + 0.5 * k1)
    k3 = h * f(t + 0.5 * h, x + 0.5 * k2)
    k4=  h * f(t + 0.5 * h, x + k3)
    return x + 1./6 * (k1 + 2 * k2 + 2 * k3 + k4)
def euler(f, t, x, h):
    return x + h * f(t, x)

# d^2/dt^2 x(t) = -x(t)     x[0] is position x[1]: velocity

def simple_pendulum(t, x):
    res = 0. * x # np.zeros(x.size, dtype= type(x[0]))
    res[0] = x[1]
    res[1] = - x[0]
    return res

vt, X = integrator(simple_pendulum, euler, 0.0, 20., np.array([1., 0., 0.]), 3000)
vt, X_runga2 = integrator(simple_pendulum, runge_kutta2, 0.0, 20., np.array([1., 0., 0.]), 3000)
vt, X_runga4 = integrator(simple_pendulum, runge_kutta4, 0.0, 20., np.array([1., 0., 0.]), 3000)

plt.plot(vt, X[:, 0])
plt.plot(vt, 1.02*X_runga2[:, 0], "--")
plt.plot(vt, X_runga4[:, 0])
plt.plot(vt, np.cos(vt))
plt.show()

print((np.abs(X[:, 0] - np.cos(vt))).max())
print((np.abs(X_runga2[:, 0] - np.cos(vt))).max())
print((np.abs(X_runga4[:, 0] - np.cos(vt))).max())