import matplotlib.pyplot as plt

f = open("dow.txt", "r")
lines = f.readlines()
prices = []
for line in lines:
    prices.append(float(line))

plt.figure()
plt.plot(range(len(prices)),prices)
plt.xlabel("time")
plt.ylabel("Dow Jones")
plt.show()