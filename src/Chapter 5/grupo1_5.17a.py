from numpy import exp, linspace
from matplotlib.pyplot import plot, show

def Integrand(a, x):
    return (x**(a-1))*exp(-x)


x = linspace(0, 5, 500)
for a in [2, 3, 4]:
    plot(x, Integrand(a, x))
    
show()