import matplotlib.pyplot as plt
from numpy.fft import rfft, irfft
from numpy import array

#parte a
f = open("dow.txt", "r")
lines = f.readlines()
prices = []
for line in lines:
    prices.append(float(line))

plt.figure()
plt.plot(range(len(prices)),prices)
plt.show()

#parte b
c = rfft(prices)

#parte c
c = array(c)
c[(int(0.1*len(c))):len(c)] = 0

#parte d
p = irfft(c)
plt.figure()
plt.plot(range(len(p)),p)
plt.show()

plt.figure()
plt.plot(range(len(prices)),prices)
plt.plot(range(len(p)),p)
plt.show()


#parte e
c = array(rfft(prices))
c[(int(0.02*len(c))):len(c)] = 0

p = irfft(c)
plt.figure()
plt.plot(range(len(p)),p)
plt.show()

plt.figure()
plt.plot(range(len(prices)),prices)
plt.plot(range(len(p)),p)
plt.show()