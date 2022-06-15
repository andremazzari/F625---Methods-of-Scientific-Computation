

#parametros do problema
a = 1
b = 2

#define x(x,y)
def X(x,y):
    return y*(a+x**2)

#define y(x,y)
def Y(x,y):
    return b/(a+x**2)

#valor inicial
x0=2.1
y0=0.4

for k in range(20):
    Xtemp = X(x0,y0)
    Ytemp = Y(x0,y0)
    x0 = Xtemp
    y0 = Ytemp
    print(x0,y0)