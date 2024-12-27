import numpy as np
import matplotlib.pyplot as plt

def mapper_QPSK(bit_1, bit_2):
    I = 0
    Q = 0
    
    if bit_1 == 0:
        if bit_2 == 0:
            I = 1
            Q = 1
        elif bit_2 == 1:
            I = -1
            Q = -1
    elif bit_1 == 1:
        if bit_2 == 0:
            I = -1
            Q = 1
        elif bit_2 == 1:
            I = 1
            Q = -1
    
    return I, Q

data = np.random.randint(0, 2, 50)

I = []
Q = []
symbols = []

for i in range(0, len(data), 2):
    I_val, Q_val = mapper_QPSK(data[i], data[i + 1])
    I.append(I_val)
    Q.append(Q_val)
    
I_with_zeros = []
Q_with_zeros = []

for i_val, q_val in zip(I, Q):
    I_with_zeros.extend([i_val] + [0] * 9)
    Q_with_zeros.extend([q_val] + [0] * 9)

I_with_zeros = np.array(I_with_zeros)
Q_with_zeros = np.array(Q_with_zeros)
    
h = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

I_arr = np.convolve(I_with_zeros, h)
Q_arr = np.convolve(Q_with_zeros, h)

plt.figure(figsize=(13, 10))
plt.subplot(2, 1, 1)
plt.title("I")
plt.stem(I_arr)

plt.subplot(2, 1, 2)
plt.title("Q")
plt.stem(Q_arr)

#I_arr *= 2 ** 14
#Q_arr *= 2 ** 14

np.savetxt("single_adalm_rx_I_arr.txt", I_arr, fmt='%d')
np.savetxt("single_adalm_rx_Q_arr.txt", Q_arr, fmt='%d')

#for i in range (len(I)):
#    symbols.append(I[i] + 1j * Q[i])
    
#samples = np.repeat(symbols, 10)
#samples *= 2 ** 14
    
#plt.stem(samples)
#plt.xlim(0, 100)

#plt.scatter(samples.real,samples.imag)
#np.savetxt("single_adalm_rx_I_arr.txt", I_arr, fmt='%d')
#np.savetxt("single_adalm_rx_Q_arr.txt", Q_arr, fmt='%d')