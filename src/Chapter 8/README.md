# Chapter 8 - Ordinary differential equations

## Exercise 8.3:
The Lorenz equations were one of the first one of the first incontrovertible examples of deterministic chaos, which is the occurrence of apparently random motion
even though there is no randomness built into the equations. They are given by the following set of differential equations:
$$ \frac{\mathrm{d} x}{\mathrm{~d} t}=\sigma(y-x), \quad \frac{\mathrm{d} y}{\mathrm{~d} t}=r x-y-x z, \quad \frac{\mathrm{d} z}{\mathrm{~d} t}=x y-b z, $$
with $\sigma=10$, $r=28$, and $b= \frac{8}{3}$ in this exercise. I used the **fourth-order Runge-Kutta** method to solve these equations with initial conditions $(x,y,z) = (0,1,0)$. In the images below, it is shown the graphs of $y$ against $t$ and of $z$ againts $x$. This last one is the famous "strange attractor" of Lorenz equations.
```diff
- colocar imagens. Adicionar titulo e axis labels.
```

## Exercise 8.10:
In this exercise, I had to calculate numerically the orbit of a comet around the sun. This is a situation which an **adaptive step size method** is useful, since the comet travels slowly when it is far from the sun and hence we can use large step sizes in this region, while the comet travels faster near the sun and small step sizes are needed.
```diff
- colocar imagem da trajetoria
```
The trajetory of the comet is described by the Newtonian gravitational force and Newton's seconod law:
$$\frac{\mathrm{d}^{2} x}{\mathrm{~d} t^{2}}=-G M \frac{x}{(x^2 + y^2)^{\frac{3}{2}}}, \quad \frac{\mathrm{d}^{2} y}{\mathrm{~d} t^{2}}=-G M \frac{y}{(x^2 + y^2)^{\frac{3}{2}}}.$$
This is a system of second order ordinary differential equations. To solve it, we transform it in a system of 4 first order differential equations by using the substitutions $u = \frac{\mathrm{d} x}{\mathrm{~d} t}$ and $w = \frac{\mathrm{d} y}{\mathrm{~d} t}$, getting the following system:
$$\frac{\mathrm{d} u}{\mathrm{~d} t} = -G M \frac{x}{(x^2 + y^2)^{\frac{3}{2}}}, \quad \frac{\mathrm{d} x}{\mathrm{~d} t} = u$$
$$\frac{\mathrm{d} w}{\mathrm{~d} t} = -G M \frac{y}{(x^2 + y^2)^{\frac{3}{2}}}, \quad \frac{\mathrm{d} y}{\mathrm{~d} t} = w$$
First, I implemented the **fourth-order Runge-Kutta** method with a fixed step size (file 8.10b.py). After some complete orbits, it is possible to note the erros in the trajetory, and for a long time the trajetory diverges completely. This is shown in the image below:
```diff
- adicionar imagem
```
Then, I implemented the **fourth-order Runge-Kutta with adaptive step size**. In this method, we choose a target error in each step and the step size is updated to reach for this error. So if in a step the error is bigger than desired, we repeat the calculations with a smaller step size. But if the error is smaller than desired, we perform the next step with a bigger step size. With this method, it was possible to reach a much better precision with much less time compared to the method with a fixed step size. So the method with adaptive step size was superior.
```diff
- adicionar e explicar imagem.
```
