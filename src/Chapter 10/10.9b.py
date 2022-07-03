from numpy import empty,sum,zeros,array,exp
from random import random,randrange
from matplotlib.pyplot import plot,show,ylabel
from time import time

#parametros do problema
Nx = 20 #numero de spins na direção x
Ny = 20 #numero de spins na direção y
J = 1

#função para calcular a energia
def Energy(s):
    E = 0
    SumRight = empty([Ny-1], int)
    SumBelow = empty([Ny], int)
    for i in range(Nx):
        SumRight[0:Ny-1] = s[i][0:Ny-1]*s[i][1:Ny]
        E += sum(SumRight)
        if i != Nx-1:
            SumBelow[0:Ny] = s[i][0:Ny]*s[i+1][0:Ny]
            E += sum(SumBelow)
    return (-1)*J*E

#matriz com os valores dos spins
s = empty([Nx,Ny], int)

#inicializa s com valores aleatorios
for i in range(Nx):
    for j in range(Ny):
        if random()<0.5:
            s[i][j] = -1
        else:
            s[i][j] = 1

E = Energy(s)
Eplot = [E]
t0 = time()
#Realiza o algoritmo de metropolis
for i in range(100000):
    #escolhe um spin para flipar
    x = randrange(Nx)
    y = randrange(Ny)
    
    #flipa o spin escolhido
    s[x][y] *= -1
    
    #calcula a nova energia e a variaçao dela
    Eprime = Energy(s)
    dE = Eprime - E
    
    #decide se mantem a mudança
    if random()<exp(-dE):
        E = Eprime #mudança aceita
    else:
        s[x][y] *= -1 #mudança rejeitada
        
    Eplot.append(E)

plot(Eplot)
ylabel("Energy")
show()
print(time()-t0)

