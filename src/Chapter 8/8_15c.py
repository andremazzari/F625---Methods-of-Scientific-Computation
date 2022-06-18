from vpython import sphere,vector,cylinder,rate
from math import sin,cos,pi
from numpy import array,arange
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

t0 = time()
r = array([pi/2,pi/2,0,0],float) #condições iniciais
for t in tpoints:
    Theta1Points.append(r[0])
    Theta2Points.append(r[1])
    
    
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6


pos1 = vector(l*sin(Theta1Points[0]),-l*cos(Theta1Points[0]),0)
pos2 = vector(l*sin(Theta2Points[1]),-l*cos(Theta2Points[1]),0)
mass1 = sphere(pos=pos1,radius=0.1)
mass2 = sphere(pos=(pos1+pos2),radius=0.1)
rod1 = cylinder(pos=vector(0,0,0), axis=pos1, radius=0.01)
rod2 = cylinder(pos=pos1, axis=pos2, radius=0.01)

for i in arange(N):
    rate(N/100)
    pos1 = vector(l*sin(Theta1Points[int(i)]),-l*cos(Theta1Points[int(i)]),0)
    pos2 = vector(l*sin(Theta2Points[int(i)]),-l*cos(Theta2Points[int(i)]),0)
    mass1.pos = pos1
    mass2.pos = pos1 + pos2
    rod1.axis = pos1
    rod2.pos = pos1
    rod2.axis = pos2
    


