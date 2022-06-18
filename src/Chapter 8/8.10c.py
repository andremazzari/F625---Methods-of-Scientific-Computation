from numpy import array,arange,sqrt,isnan,power,copy
import matplotlib.pyplot as plt
import matplotlib as mpl
from time import time

#constantes do problema
M = 1.99e30 #Massa do sol em kg
G = 66.33e-6 #Constante gravitacional em (km)^3(kg)^-1(ano)^-2

# r[0]=x ; r[1]=y ; r[2]=dx/dt=u r[3]=dy/dt=w
def f(R,t):
    x = R[0]
    y = R[1]
    u = R[2]
    w = R[3]
    fx = u
    fy = w
    fu = -(G*M*x)/(sqrt(x**2 + y**2)**3)
    fw = -(G*M*y)/(sqrt(x**2 + y**2)**3)
    return array([fx,fy,fu,fw],float)

def runge_kutta(r,h,t):
    v = copy(r)
    k1 = h*f(v,t)
    k2 = h*f(v+0.5*k1,t+0.5*h)
    k3 = h*f(v+0.5*k2,t+0.5*h)
    k4 = h*f(v+k3,t+h)
    v += (k1+2*k2+2*k3+k4)/6
    return v

a = 0.0
b = 1000
N = 1e4
h = (b-a)/N #Valor inicial do passo
delta = 1

xpoints = []
ypoints = []


r = array([4e9, 0.0, 0.0, 15.768e6],float) #Condiçoes iniciais no sistema SI

#salva as condições iniciais
xpoints.append(r[0])
ypoints.append(r[1])

t = a

t0=time()
i=0 #numero de passos
while (t<b):
    
    flag = 0
    while flag == 0:

        #faz a primeira estimativa
        r0 = runge_kutta(r,h,t)
        r1 = runge_kutta(r0,h,t+h)
        r2 = runge_kutta(r,2*h,t)        
        
        #calcula o erro
        e = (r1[0] - r2[0])**2 + (r1[1] - r2[1])**2
        
        if e != 0:
            p = (30*h*delta)/sqrt(e)
        else: #o valor de p deveria ser infinito
            p=1 + 2*h #faz com que p tenha um valor mairo que 2*h, para que no proximo bloco h = 2*h
            #print(i)
            
        if p>=1:
            #precisão melhor que a desejada
            t += 2*h
            
            if power(p,1/4) > 2:
                h = 2*h
            else:
                h = h*power(p,1/4)
            
            flag = 1
            #if i>1467:
              #  print(1,i,h,p,t,r0[1],r1[1])
        elif p<1:
            #precisão pior que a desejada
            h = h*p**(1/4)
            #if i>1467:
               # print(2,i,h,p,t)


    xpoints.append(r0[0])
    ypoints.append(r0[1])
    
    xpoints.append(r1[0])
    ypoints.append(r1[1])
    i+=1

    
    r = r1


plt.plot(xpoints,ypoints)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print(time()-t0)
print(i)
