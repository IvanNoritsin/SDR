import numpy as np
import matplotlib.pyplot as plt

A = 2  
f = 5  
phi = 0
T = 1 / f  
Ts = 0.01  
t = np.arange(0, T, Ts)

x = A * np.cos(2 * np.pi * f * t + phi)

plt.figure(figsize=(10, 6))
plt.plot(t, x, label='x(t)')
plt.title('Гармоническое колебание x(t)')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()

n_vals = np.arange(0, 5)
a_n = []
b_n = []

for n in n_vals:
    cos_n = np.cos(2 * np.pi * n * f * t)
    sin_n = np.sin(2 * np.pi * n * f * t)
    
    a_n_val = (2 / T) * np.sum(x * cos_n) * Ts
    b_n_val = (2 / T) * np.sum(x * sin_n) * Ts
    print(f"a_{n} = {a_n_val:.4f}; b_{n} = {b_n_val:.4f}")
    
    a_n.append(a_n_val)
    b_n.append(b_n_val)
    
a_n = np.array(a_n)
b_n = np.array(b_n)

a_n[np.abs(a_n) < 1e-7] = 0
b_n[np.abs(b_n) < 1e-7] = 0    

A_n = np.sqrt(np.array(a_n)**2 + np.array(b_n)**2)
phi_n = np.arctan2(b_n, a_n)


plt.figure(figsize=(10, 6))
plt.stem(n_vals, A_n)
plt.title('Спектр амплитуд (начальная фаза = )')
plt.xlabel('n')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.stem(n_vals, phi_n)
plt.title('Спектр фаз (начальная фаза = )')
plt.xlabel('n')
plt.ylabel('Фаза (рад)')
plt.grid(True)
plt.show()
