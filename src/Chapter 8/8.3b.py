from numpy import array,arange
from pylab import plot,xlabel,show

A = 10
B = 28
C = 8/3

def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = A*(y - x)
    fy = B*x - y - x*z
    fz = x*y - C*z
    return array([fx,fy,fz],float)

a = 0.0
b = 50.0
N = 100000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

r = array([0.0,1.0,0.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(xpoints,zpoints)
show()
