from numpy import loadtxt,zeros,cos,sin,pi,sqrt
import matplotlib.pyplot as plt

w = loadtxt("stm.txt",float)
#Este vetor altitude possui 663 lilnhas e 676 colunas
#Estou considerando que o primeiro indice, das linhas, representa a variação na variavel x
#E, portanto, variar o segundo indice seria variar a variavel y.
print(len(w))
print(len(w[0]))
#arrays em que serão salvos os valores das derivadas parciais.
Dx = zeros((663,676))
Dy = zeros((663,676))

#Para calcular as derivadas, usarei difrenças centrais no interior do conjunto de pontos,
#e nas extremidades usarei diferenças foward or backward diferences.
#O espaçamento entre os pontos é dado do problema, h=30000

h=2.5

#Primeiro calcula as derivadas em relação a x
for y in range(676):
    for x in range(663):
        if x==0: #forward diference
            Dx[x][y] = (w[x+1][y]-w[x][y])/h
        elif x==662: #backward diference
            Dx[x][y] = (w[x][y]-w[x-1][y])/h
        else: #Central diference.
            Dx[x][y] = (w[x+1][y]-w[x-1][y])/(2*h)
            
#Agora calcula as derivadas em relação a y
for x in range(663):
    for y in range(676):
        if y==0: #forward diference
            Dx[x][y] = (w[x][y+1]-w[x][y])/h
        elif y==675: #backward diference
            Dx[x][y] = (w[x][y]-w[x][y-1])/h
        else: #Central diference.
            Dx[x][y] = (w[x][y+1]-w[x][y-1])/(2*h)

#Vamos calcular agora a intensidade em cada ponto
#Para isto, criamos um array para armazenar este valor em cada ponto
CosPhi = cos(pi/4)
SinPhi = sin(pi/4)
I = zeros((663,676))
for x in range(663):
    for y in range(676):
        I[x][y] = (CosPhi*Dx[x][y] + SinPhi*Dy[x][y])/sqrt(Dx[x][y]**2 + Dy[x][y]**2 + 1)

plt.gray()
plt.imshow(I)