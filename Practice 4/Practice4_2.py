import numpy as np
import matplotlib.pyplot as plt

A = 1
f0 = 0.5
T = 1 / f0
Ts = 0.01
t = np.arange(0, 5, Ts)

x_t = np.where((t % T) < (T / 2), A, 0)

plt.figure()
plt.plot(t, x_t)
plt.title('Периодический прямоугольный сигнал')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()

n_vals = np.arange(1, 7)
a_n = []
b_n = []

a0 = (1 / T) * np.sum(x_t) * Ts

for n in n_vals:
    cos_n = np.cos(2 * np.pi * n * f0 * t)
    sin_n = np.sin(2 * np.pi * n * f0 * t)

    a_n_val = (2 / T) * np.sum(x_t * cos_n) * Ts
    b_n_val = (2 / T) * np.sum(x_t * sin_n) * Ts
    print(f"a_{n} = {a_n_val:.4f}; b_{n} = {b_n_val:.4f}")
    
    a_n.append(a_n_val)
    b_n.append(b_n_val)


a_n = np.array(a_n)
b_n = np.array(b_n)

a_n[np.abs(a_n) < 1e-7] = 0
b_n[np.abs(b_n) < 1e-7] = 0
    

A_n = np.sqrt(np.array(a_n)**2 + np.array(b_n)**2)
phi_n = -(np.arctan2(b_n, a_n))

x_reconstructed = np.zeros_like(t)

for n in range(len(n_vals)):
    x_reconstructed += A_n[n] * np.cos(2 * np.pi * (n_vals[n]) * f0 * t + phi_n[n])
    
x_reconstructed += a0

plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label='Исходный сигнал', linestyle='--', color='red')
plt.plot(t, x_reconstructed, label='Восстановленный сигнал', color='blue')
plt.title('Сравнение оригинального и восстановленного сигналов')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.stem(n_vals, A_n)
plt.title('Амплитуды A_n для прямоугольного сигнала')
plt.xlabel('Номер гармоники n')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.stem(n_vals, phi_n)
plt.title('Фазы ϕ_n для прямоугольного сигнала')
plt.xlabel('Номер гармоники n')
plt.ylabel('Фаза (рад)')
plt.grid(True)
plt.show()
