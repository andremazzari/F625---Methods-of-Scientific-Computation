from numpy import array,arange,sqrt
import matplotlib.pyplot as plt
from time import time

#constantes do problema
M = 1.99e30 #Massa do sol em kg
G = 66.33e-6 #Constante gravitacional em (km)^3(kg)^-1(ano)^-2

# r[0]=x ; r[1]=y ; r[2]=dx/dt=u r[3]=dy/dt=w
def f(r,t):
    x = r[0]
    y = r[1]
    u = r[2]
    w = r[3]
    fx = u
    fy = w
    fu = -(G*M*x)/sqrt(x**2 + y**2)**3
    fw = -(G*M*y)/sqrt(x**2 + y**2)**3
    return array([fx,fy,fu,fw],float)

a = 0.0
b = 600
N = 5e5
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([4e9, 0.0, 0.0, 15.768e6],float) #Condiçoes iniciais no sistema SI
t0 = time()
for t in tpoints:
    
    xpoints.append(r[0])
    ypoints.append(r[1])
    
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
    

plt.plot(xpoints,ypoints)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print(time()-t0)
