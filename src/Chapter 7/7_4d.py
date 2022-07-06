from numpy.fft import rfft,irfft
from numpy import array
import matplotlib.pyplot as plt
import os

path = os.path.dirname(__file__)

f = open(path + "/dow.txt", "r")
lines = f.readlines()
prices = []
for line in lines:
    prices.append(float(line))

c = rfft(prices)

c = array(c)
c[(int(0.1*len(c))):len(c)] = 0

p = irfft(c)

plt.figure()
plt.plot(range(len(prices)),prices, label = "Original curve")
plt.plot(range(len(p)),p, label = "Curve after processing")
plt.xlabel("Time")
plt.ylabel("Dow Jones")
plt.title("90% of the Fourier coefficients discarted")
plt.legend()
plt.show()
