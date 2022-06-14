# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:14:00 2019

@author: Andre
"""
from numpy import linspace,pi,sqrt,zeros
from matplotlib.pyplot import imshow,show,jet

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

V = zeros((101,101)) #array em que serão salvos os valores dos potenciais
kx = 0 #contador da posiçao x no array data
for x in linspace(-0.5,0.5,101):
    ky = 0 #contador da posiçao y no array data
    for y in linspace(-0.5,0.5,101):
        if x==x1 and y==y1: #verifica se está na posição da carga 1
            V[kx][ky] = V2(x,y)
        elif x==x2 and y==y2: #verifica se está na posição da carga 2
            V[kx][ky] = V1(x,y)
        else:
            V[kx][ky] = V1(x,y) + V2(x,y)
        ky += 1
    kx += 1

jet()
imshow(V)
show()