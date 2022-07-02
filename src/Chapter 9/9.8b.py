from numpy import empty,exp,copy,linspace,stack
from vpython import gcurve,rate,color,graph

def banded(Aa,va,up,down):

    # Copy the inputs and determine the size of the system
    A = copy(Aa)
    v = copy(va)
    N = len(v)

    # Gaussian elimination
    for m in range(N):

        # Normalization factor
        div = A[up,m]

        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]

        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]

    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]

    return v

#parametros do problema
m = 9.109e-31 #Massa do eletron em kg
L = 1e-8 #Largura da caixa em metros
N = 1000 #Numero de divisoes no reticulado
a = L/N #Distancia entre os pontos do reticulado em metros
sigma = 1e-10 #metros
kappa = 5e10 #metros^-1
h = 1e-18 #intervalo de tempo em segundos
hbar = 1.05457e-34 #constante de planck reduzida em J*s

psi = empty([N+1], complex)
psiprime = empty([N+1], complex)
v = empty([N+1], complex)
a1 = complex(1,h*hbar/(2*m*a**2))
a2 = complex(0,-h*hbar/(4*m*a**2))
b1 = complex(1,-h*hbar/(2*m*a**2))
b2 = complex(0,h*hbar/(4*m*a**2))

#inicializa o vetor psi nos valores iniciais(t=0)
for i in range(N+1):
    if i==0 or i==N:
        psi[i] = 0
    else:
        psi[i] = exp(-(i*a-L/2)**2/(2*sigma**2))*exp(complex(0,kappa*i*a))

#calcula v=B*psi
for i in range(N+1):
    if i==0:
        v[i] = b1*psi[i] + b2*psi[i+1]
    elif i==N:
        v[i] = b1*psi[i] + b2*psi[i-1]
    else:
        v[i] = b1*psi[i] + b2*(psi[i+1] + psi[i-1])

#Cria a matriz A usada no código banded.py
A = empty([3,N+1], complex)
for i in range(3):
    for j in range(N+1):
        if (i==0 and j==0) or (i==2 and j==N):
            A[i][j] = 0
        elif i==1:
            A[i][j] = a1
        else:
            A[i][j] = a2

#cria o gráfico
g = graph(width=500, height=500, foreground=color.black, background=color.white, xmin=0, xmax=L, ymin=-1, ymax=1)
f1 = gcurve(color=color.cyan)
i = 0
for x in linspace(0,L,N+1):
    f1.plot(x,psi[i].real)
    i += 1
    
x = linspace(0,L,N+1)

t = 0.0
tfinal = 1e-13
while t<tfinal:
    #calcula os novos valores de psi e t+h a partir dos valores em t
    psiprime = banded(A,v,1,1)
    
    #mantem as condições de contorno
    psiprime[0] = 0
    psiprime[N] = 0
    
    #inverte as matrizes
    psi, psiprime = psiprime, psi
    
    #atualiza o gráfico
    rate(1000)
    y = psi.real
    f1.data = stack((x,y), axis=-1)
    
    
    #calcula a nova matriz v
    for i in range(N+1):
        if i==0:
            v[i] = b1*psi[i] + b2*psi[i+1]
        elif i==N:
            v[i] = b1*psi[i] + b2*psi[i-1]
        else:
            v[i] = b1*psi[i] + b2*(psi[i+1] + psi[i-1])
            
    t += h
    
    