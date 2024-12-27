import numpy as np
import matplotlib.pyplot as plt

I = []
Q = []

I_tx = []
Q_tx = []

with open('rx_signal.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        I.append(int(values[0]))
        Q.append(int(values[1]))
        


with open('single_adalm_rx_Q_arr.txt', 'r') as file:
    for line in file:
        Q_tx.append(int(line.strip())) 

with open('single_adalm_rx_I_arr.txt', 'r') as file:
    for line in file:
        I_tx.append(int(line.strip())) 

#I_p = np.array(I_tx)        
#Q_p = np.array(Q_tx)


#I //= 2 ** 8
#Q //= 2 ** 8

h = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

I_conv = np.convolve(I, h)
Q_conv = np.convolve(Q, h)


plt.figure(figsize=(13, 10))
plt.plot(I_conv)
plt.grid()

symbols = I_conv + 1j * Q_conv

plt.figure(figsize=(13, 10))
plt.scatter(symbols.real,symbols.imag)

#plt.figure(figsize=(13, 10))
#plt.subplot(2, 1, 1)
#plt.plot(I_arr)
#plt.grid()

#plt.subplot(2, 1, 2)
#plt.plot(Q_arr)
#plt.grid()

