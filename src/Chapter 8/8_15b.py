from math import sin,cos,pi
from numpy import array,arange
import matplotlib.pyplot as plt
from time import time

#parametros do problema (valores no sistema SI)
g = 9.81
l = 0.4
m = 1


def f(r,t):
    theta1 = r[0]
    theta2 = r[1]
    omega1 = r[2]
    omega2 = r[3]
    Ftheta1 = omega1
    Ftheta2 = omega2
    Fomega1 = -((omega1**2)*sin(2*theta1-2*theta2) + 2*(omega2**2)*sin(theta1-theta2) + (g/l)*(sin(theta1 - 2*theta2) + 3*sin(theta1)))/(3 - cos(2*theta1-2*theta2))
    Fomega2 = (4*(omega1**2)*sin(theta1 - theta2) + (omega2**2)*sin(2*theta1 - 2*theta2) + 2*(g/l)*(sin(2*theta1 - theta2) - sin(theta2)))/(3 - cos(2*theta1 - 2*theta2))
    return array([Ftheta1, Ftheta2, Fomega1, Fomega2],float)

a = 0.0
b = 100.0
N = 1e5
h = (b-a)/N

tpoints = arange(a,b,h)
Theta1Points = []
Theta2Points = []
Omega1Points = []
Omega2Points = []
#K = [] #Energia cinetica
#U = [] #Energia potencial
E = []

t0 = time()
r = array([pi/2,pi/2,0,0],float) #condições iniciais
#energia inicial
E0 = -m*g*l*(2*cos(r[0]) + cos(r[1])) + m*(l**2)*(r[2]**2 + 0.5*r[3]**2 + r[2]*r[3]*cos(r[0]-r[1]))
DeltaE = 0 #Variaçao de enrgia maxima
for t in tpoints:
    Theta1Points.append(r[0])
    Theta2Points.append(r[1])
    Omega1Points.append(r[2])
    Omega2Points.append(r[3])
    
    
    U = -m*g*l*(2*cos(r[0]) + cos(r[1]))
    K = m*(l**2)*(r[2]**2 + 0.5*r[3]**2 + r[2]*r[3]*cos(r[0]-r[1]))
    E.append(K + U)
    
    if (abs(E0 - K - U) >= 1e-5):
        print("passou a precisao",t)
    
    if (abs(E0 - K - U) > DeltaE):
        DeltaE = abs(E0 - K - U)    
    
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
    


plt.plot(tpoints,E)
plt.title("Variation of energy during evolution", fontsize = 12)
plt.xlabel("Time")
plt.ylabel("Energy")
plt.show()
print("Variaçao maxima de energia:",DeltaE)
print(time()-t0)
