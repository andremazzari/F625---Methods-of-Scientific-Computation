from numpy.fft import rfft


f = open("dow.txt", "r")
lines = f.readlines()
prices = []
for line in lines:
    prices.append(float(line))

c = rfft(prices)