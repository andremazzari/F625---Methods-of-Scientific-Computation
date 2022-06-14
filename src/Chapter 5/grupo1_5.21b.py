# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:14:00 2019

@author: Andre
"""
from numpy import linspace,pi,sqrt,zeros,gradient,negative
import matplotlib.pyplot as plt

Q1 = 1 #valor da carga 1
x1 = 0.05 #coordenada x da carga 1
y1 = 0 #coordenada y da carga 1
Q2 = -1 #valor da carga 2
x2 = -0.05 #coordenada x da carga 2
y2 = 0 #coordenada y da carga 2
e0 = 8.8541878176e-12 #permissividade eletrica no vacuo
C1 = Q1/(4*pi*e0) #constante no potencial da carga 1
C2 = Q2/(4*pi*e0) #constante no potencial da carga 2

#funçao que calcula o potencial gerado pela carga 1
def V1(x, y):
    r = sqrt((x1-x)**2+(y1-y)**2)
    return C1/r

#funçao que calcula o potencial gerado pela carga 2
def V2(x, y):
    r = sqrt((x2-x)**2+(y2-y)**2)
    return C2/r

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
        if x==x1 and y==y1: #verifica se está na posição da carga 1
            V[kx][ky] = V2(x,y)
        elif x==x2 and y==y2: #verifica se está na posição da carga 2
            V[kx][ky] = V1(x,y)
        else:
            V[kx][ky] = V1(x,y) + V2(x,y)
        ky += 1
    kx += 1

dx = (Xmax-Xmin)/(DivX-1) #espaço entre os pontos na coordenada x
dy = (Xmax-Xmin)/(DivY-1) #espaço entre os pontos na coordenada y
E = negative(gradient(V, dx, dy)) #calcula o campo eletrico

plt.streamplot(linspace(Xmin,Xmax,DivX), linspace(Ymin,Ymax,DivY), E[1], E[0], density = 2)