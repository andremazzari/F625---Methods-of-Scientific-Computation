from numpy import sqrt,sin,pi,linspace,ones,copy,cos,tan,zeros,negative,gradient
import matplotlib.pyplot as plt

#parametros do problema
q0 = 100 #Em Coulomb por metro^2
L = 0.1 #Em metros

#funções de integração gaussiana. Foram usados códigos do livro disponiveis nos arquivos gaussint.py e gaussxw.py
def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

#parametros da integração gaussiana
N = 5
a = -0.05
b = 0.05
x,w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

#Define o integrando utilizado para se calcular o potencial em um ponto
#As coordenadas (x1,y1) se referem ao ponto no espaço em que estamos calculado o potencial
#As coordenadas (x2,y2) se referem ao ponto da distribuiçao de carga que estamos usando no calculo do potencial
def Integrando(x1,y1,x2,y2):
    r = sqrt((x1-x2)**2+(y1-y2)**2)
    return (q0*sin((2*pi*x2)/L)*sin((2*pi*y2)/L))/r

#Define a função que calcula o potencial em um dado ponto (x,y)
def Potencial(x,y):
    potencial = 0.0
    for ny in range(N):
        for nx in range(N):
            potencial += wp[ny]*wp[nx]*Integrando(x,y,xp[nx],xp[ny])
        #potencial = wp[ny]*potencial
    return potencial

#parametros da área em que serao feitos os calculos
Xmax = 0.5 #coordenada x maxima
Xmin = -0.5 #coordenada x minima
Ymax = 0.5 #coordenada y maxima
Ymin = -0.5 #coordenada y minima
DivX = 101 #numero que pontos na coordenada x
DivY = 101 #numero de pontos na coordenada y

V = zeros((DivX,DivY)) #array em que serão salvos os valores dos potenciais
kx = 0 #contador da posiçao x no array data
for x in linspace(Xmin,Xmax,DivX):
    ky = 0 #contador da posiçao y no array data
    for y in linspace(Ymin,Ymax,DivY):
        V[kx][ky] = Potencial(x,y)
        ky += 1
    kx += 1

plt.figure()
plt.imshow(V)

 
 
dx = (Xmax-Xmin)/(DivX-1) #espaço entre os pontos na coordenada x
dy = (Xmax-Xmin)/(DivY-1) #espaço entre os pontos na coordenada y
E = negative(gradient(V, dx, dy)) #calcula o campo eletrico

plt.figure()
plt.streamplot(linspace(Xmin,Xmax,DivX), linspace(Ymin,Ymax,DivY), E[1], E[0], density = 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Streamplot of the electric field", fontsize = 15)
plt.show()