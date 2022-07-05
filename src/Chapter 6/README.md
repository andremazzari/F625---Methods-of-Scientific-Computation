# Chapter 6 - Solution of linear and nonlinear equations

## Exercise 6.12:
In this exercise, we need to <b>solve numerically the nonlinear equations</b> that describe the process of breakdown of glucose in the body to release energy:
$$ \frac{\mathrm{d} x}{\mathrm{~d} t}=-x+a y+x^{2} y, \quad \frac{\mathrm{d} y}{\mathrm{~d} t}=b-a y-x^{2} y , $$
where $x$ and $y$ represents the concentrations of ADP and F6P, respectively, and $a$ and $b$ are positive constants (in what follows, $a=1$ and $b=2$ to solve the equations). We want to find stationary points for these equations, i.e. we want $x$ and $y$ such that the derivatives of these functions concerning time are null. From the equations above we see that this also means finding the solution to the equations
$$-x+a y+x^{2} y=0, \quad b-a y-x^{2} y=0. $$
To solve these nonlinear equations, I used the <b>relaxation method</b>. First, I wrote the equations as
$$ x=y\left(a+x^{2}\right), \quad y=\frac{b}{a+x^{2}}. $$
But the relaxation method did not converged to a solution. So I tried to rewrite the equations in another form:
$$x=\sqrt{\frac{b}{y}-a}, \quad y=\frac{x}{a+x^{2}}.$$
With the equations written in this form, the relaxation method converged to near the exact solutions $x=2$ and $y=0.4$.
