from numpy.fft import rfft,irfft
from numpy import array
import matplotlib.pyplot as plt

f = open("dow.txt", "r")
lines = f.readlines()
prices = []
for line in lines:
    prices.append(float(line))

c = rfft(prices)

c = array(c)
c[(int(0.02*len(c))):len(c)] = 0

p = irfft(c)

plt.figure()
plt.plot(range(len(prices)),prices)
plt.plot(range(len(p)),p)
plt.xlabel("time")
plt.ylabel("Dow Jones")
plt.show()
