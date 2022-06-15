from numpy import loadtxt,zeros,cos,sin,pi,sqrt
import matplotlib.pyplot as plt

altitude = loadtxt("altitude.txt",float)
#Este vetor altitude possui 512 lilnhas e 1024 colunas
#Estou considerando que o primeiro indice, das linhas, representa a variação na variavel x
#E, portanto, variar o segundo indice seria variar a variavel y.

#arrays em que serão salvos os valores das derivadas parciais.
Dx = zeros((512,1024))
Dy = zeros((512,1024))

#Para calcular as derivadas, usarei difrenças centrais no interior do conjunto de pontos,
#e nas extremidades usarei diferenças foward or backward diferences.
#O espaçamento entre os pontos é dado do problema, h=30000

h=30000

#Primeiro calcula as derivadas em relação a x
for y in range(1024):
    for x in range(512):
        if x==0: #forward diference
            Dx[x][y] = (altitude[x+1][y]-altitude[x][y])/h
        elif x==511: #backward diference
            Dx[x][y] = (altitude[x][y]-altitude[x-1][y])/h
        else: #Central diference.
            Dx[x][y] = (altitude[x+1][y]-altitude[x-1][y])/(2*h)
            
#Agora calcula as derivadas em relação a y
for x in range(512):
    for y in range(1024):
        if y==0: #forward diference
            Dx[x][y] = (altitude[x][y+1]-altitude[x][y])/h
        elif y==1023: #backward diference
            Dx[x][y] = (altitude[x][y]-altitude[x][y-1])/h
        else: #Central diference.
            Dx[x][y] = (altitude[x][y+1]-altitude[x][y-1])/(2*h)