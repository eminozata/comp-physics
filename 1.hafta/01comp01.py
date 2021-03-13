import numpy as np
import matplotlib.pyplot as plt

vx = np.zeros(21, dtype=float)

vx[0] = 1.0
vx[1] = 0.1

for k in range(2,21):
    vx[k] = 10.1 * vx[k-1] - vx[k-2]
    #print(vx[k])

x0 = 1.0
x1 = 0.1
## fazla hafıza harcamadan
for k in range(2,21):
    x2 = 10.1 * x1 - x0
    print("k = ", k ," ",  x2)
    x0 = x1
    x1 = x2


