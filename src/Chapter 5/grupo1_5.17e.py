from numpy import ones,copy,cos,tan,pi,linspace,log,exp


#parametros do problema
A = 0.5 #valor que se deseja calcular a função gamma. Deve ser maior que zero.
c = A-1

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

def f(z):
    if A > 1: #caso em que A maior que 1
        x = (c*z)/(1-z)
        expoente = (A-1)*log(x) - x
        return (c*exp(expoente))/(1-z)**2
    elif A < 1: #caso em que A menor do que 1
        x = (0.1*z)/(1-z)
        expoente = (A-1)*log(x) - x
        return 0.1*(exp(expoente))/(1-z)**2
    else: #caso A igual a 1
        x = (0.1*z)/(1-z)
        return 0.1*(exp(-x))/(1-z)**2
    
N = 15
a = 0.0
b = 1.0

# Calculate the sample points and weights, then map them
# to the required integration domain
x,w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

# Perform the integration
s = 0.0
for k in range(N):
    s += wp[k]*f(xp[k])
    
print(s)