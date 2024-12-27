import numpy as np 
import matplotlib.pyplot as plt 

fm = 300
fc = 10 * fm
fs = 2 * fc 
Ts = 1 / fs
t = np.linspace(0, 15*10^(-2), 1000) * Ts

y = 2 * np.cos(2 * np.pi * fm * t) * np.cos(2 * np.pi * fc * t) - np.sin(2 * np.pi * fm * t) * np.sin(2 * np.pi * fc * t)

I = 2 * np.cos(2 * np.pi * fm * t)
Q = np.sin(2 * np.pi * fm * t)

z = np.sqrt(I**2 + Q**2)
arctg = np.arctan(Q/I)

plt.figure(figsize=(15, 10))
plt.subplot(2, 1, 1)
plt.plot(y)
plt.plot(arctg, color='red')

plt.subplot(2, 1, 2)
plt.plot(y)
plt.plot(z, color='green')