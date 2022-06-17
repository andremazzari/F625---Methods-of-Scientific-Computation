from numpy.fft import rfft
from numpy import array

f = open("dow.txt", "r")
lines = f.readlines()
prices = []
for line in lines:
    prices.append(float(line))

c = rfft(prices)

c = array(c)
c[(int(0.1*len(c))):len(c)] = 0