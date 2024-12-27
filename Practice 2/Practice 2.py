import numpy as np
import adi
import matplotlib.pyplot as plt

sdr = adi.Pluto('ip:192.168.2.1')  # Убедитесь, что IP-адрес правильный
sdr.sample_rate = int(2.5e6)
sdr.rx_lo = int(2e9)
sdr.tx_lo = int(2e9)

rectangle = []
for i in range(1024):
    if i < 300 or i > 700:
        rectangle.append(complex(0, 0))
    else:
        rectangle.append(complex(4000, 0))

big_array = []
for i in range(1000):
    sdr.tx(rectangle)
    big_array.append(sdr.rx())

# Преобразуем big_array в массив NumPy для обработки
big_array = np.array(big_array)

# Визуализация
plt.figure(figsize=(12, 6))

# Подграфик для переданного сигнала
plt.subplot(2, 1, 1)
plt.plot(np.abs(rectangle))
plt.title('Transmitted Signal (Amplitude)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid()

# Подграфик для принятого сигнала
plt.subplot(2, 1, 2)
plt.plot(np.abs(big_array))
plt.title('Received Signal (Amplitude)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()  # Чтобы избежать наложения подграфиков
plt.show()
