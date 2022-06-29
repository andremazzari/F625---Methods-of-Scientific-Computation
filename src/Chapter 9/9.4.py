from numpy import empty,sin,pi, linspace
from matplotlib.pyplot import plot,xlabel,ylabel,show,legend
from time import time

#parametros do problema
L = 20 #altura máxima em metros
N = 100 #número de divisões do reticulado
a = L/N #espaçmento do reticulado em metros
D = 0.1 #constante de difusão em m^2day^-1
A = 10 #em graus celsius
B = 12 #em graus celsius
tau = 365 #periodo em dias
h = 0.1 #passo em dias
epsilon = h/1000 #em dias, usado para comparar as datas
c = (h*D)/(a**2) #coeficiente usado no sistema de equações
profundidade = linspace(0,L,N+1)

#arrays em que serão salvas as temperaturas
T = empty([N+1], float)
Tprime = empty([N+1], float)

#define os tempos relevantes
t = 0.0
tfinal = 10*365 #10 anos em dias
t1 = 9*365 + 91 #9 anos e 3 meses
t2 = t1 + 91 #9 anos e 6 meses
t3 = t2 + 91 #9 anos e 9 meses
t4 = t3 + 92 #10 anos
t0 = time()


#inicializa com os valores iniciais
for i in range(0,N+1):
    if i==0:
        T[i] = A + B*sin(2*pi*t/tau)
    elif i==N:
        T[i] = 11
        Tprime[i] = 11
    else:
        T[i] = 10

while t<(tfinal):
    #atualiza a condição de contorno na superficie
    Tprime[0] = A + B*sin(2*pi*(t+h)/tau)
    
    #atualiza no interior
    Tprime[1:N] = T[1:N] + c*(T[0:N-1] + T[2:N+1] - 2*T[1:N])
    
    #inverte os arrays
    T, Tprime = Tprime, T
    
    t += h
    
    #plota as temperaturas nos tempos definidos
    if abs(t-t1)<epsilon:
        plot(profundidade,T, label = "9 anos e 3 meses")
    elif abs(t-t2)<epsilon:
        plot(profundidade,T, label = "9 anos e 6 meses")
    elif abs(t-t3)<epsilon:
        plot(profundidade,T, label = "9 anos e 9 meses")
    elif abs(t-t4)<epsilon:
        plot(profundidade,T, label = "10 anos")

xlabel("profundidade(m)")
ylabel("temperatura(Celsius)")
legend()
show()
print(time()-t0)
    
    
    