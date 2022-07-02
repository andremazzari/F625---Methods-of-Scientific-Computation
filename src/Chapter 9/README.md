# Chapter 9 - Partial differential equations

## Exercise 9.4:
In this exercise, we had to calculate how the temperature varies on Earth's crost during the year from the surface to a depth of 20 m. For this, I had to solve the <b>heat equation</b>
$$ \frac{\partial T}{\partial t} = D \frac{\partial^2 T}{\partial^2 x}, $$
where $T(x,t)$ is the temperature at height $x$ ant time $t$, and $D=0.1$ $m^2$ $day^{-1}$ is the diffusion coefficient. This problem has a <b>time-varying boundary condition</b> for the temperature of the surface given by
$$T_0(t) = A + B \sin \frac{2 \pi t}{\tau},$$
with A = 10&deg;C, B = 12&deg;C and $\tau=365$ days. The other boundary condition for the temperature of the crost 20 m below the surface is a constant value of 11&deg;C. The <b>initial values</b> for the interior points are 10&deg;C. To solve this problem, I used the <b>Time-Forward Centered-Space (FTCS)</b> method. First, I calculated to solution up to 9 years to let the temperatures stabilize in the correct pattern. Then, for the tenth year, I made a plot of how the temperature varies over the crost for four different periods of the year. The result can be seen in the image below:
```diff
- Colocar imagem. Adicionar legendas em ingles e titulo.
```
One important point that I had to pay attention to was the <b>numerical stability</b>. For some choices of parameters of the FTCS method, the solution can become *unstable*. To analyze this, I used the <b>Von Neumann stability analysis</b>. Applied to the heat equation, it states that the numerical solution will be stable if the following condition is satisfied:
$$h \leq \frac{a^2}{2D},$$
  where $h$ is the temporal time step and $a$ is the grid distance between the space points.
  
  ## Exercise 9.8:
  In this exercise, I had to use the <b>Crank-Nicolson</b> method so olve the <b>time-dependent Schrodinger equation</b> in one dimension for a free particle in a box:
  $$ i \hbar \frac{\partial \psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial^2 x}.$$
  The box has length L and infinity potential walls, such that the <b>boundary conditions</b> are that the wavefunction $\psi$ is zero at $x=0$ and $x=L$. The initial condition for the wavefunction was
$$\psi (x, 0)=\exp \left[-\frac{\left(x-x_0\right)^2}{2 \sigma^2}\right] e^{i \kappa x}.$$
  In the Crank-Nicolson method, it is needed to solve a system of linear equations. Since the matrix of coefficients of the system is tridiagonal, the system can be solved very quickly (see 'Exercise 9.8:The Schrodinger equation and the Crank-Nicolson method' in '/references/exercises9.pdf' for more details). I also made an animation, using the library <b>vpython</b>, of the evolution of the wavefunction over time. Below, there are two frames of the animation:
  ```diff
  -Colocar frames
  ```
  
  
