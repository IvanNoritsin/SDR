import numpy as np
import matplotlib.pyplot as plt

fc = 1e10
Ts = 1e-3
Tsp = 5e-3

I = [1, 0, -1, 1, -1]
Q = [-1, -1, 0, 0, 1]


t = np.linspace(0, Ts, 1000)


plt.figure(figsize=(13, 10))

count
for i in range(5):
    
    cos_t = np.cos(2 * np.pi * fc * t)
    sin_t = np.sin(2 * np.pi * fc * t)
    x = I[i] * cos_t - Q[i] * sin_t
    plt.subplot(5, 1, i + 1)
    plt.plot(t, x)
    plt.grid()
    plt.xlim(0, Ts)
    

plt.figure(figsize=(13, 10))
for i in range(5):
    a = np.sqrt(I[i] ** 2 + Q[i] ** 2)
    phi = np.arctan2(Q[i], I[i])
    x = a * np.cos(2 * np.pi * fc * t + phi)
    plt.subplot(5, 1, i + 1)
    plt.plot(t, x)
    plt.grid()
    plt.xlim(0, Ts)
