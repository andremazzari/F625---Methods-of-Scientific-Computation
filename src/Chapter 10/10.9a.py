from numpy import empty,sum,zeros,array,full

#parametros do problema
Nx = 20 #numero de spins na direção x
Ny = 20 #numero de spins na direção y
J = 1

#matriz com os valores dos spins
s = full((20,20), -1)

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

print(Energy(s))