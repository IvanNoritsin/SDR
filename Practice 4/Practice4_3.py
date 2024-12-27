import numpy as np

T = 0.5
f1 = 1 / T
n = 2
Ts = 0.01
t = np.arange(0, 5, Ts)

s1 = np.sin(2 * np.pi * f1 * t)
sn = np.sin(2 * np.pi * n * f1 * t)

integ = sum(s1 * sn) * Ts
print(integ)

