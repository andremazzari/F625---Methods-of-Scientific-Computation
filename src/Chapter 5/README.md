# Chapter 5 - Integrals and derivatives

## Exercise 5.17:
The aim of this exercise is to calculate the gamma function, which is defined by
$$ \Gamma (a) = \int_{0}^{\infty} x^{a-1}e^{-x}  dx. $$
But to calculate this integral is not so straightforward. First, the range of the integral is from 0 to $\infty$, and we have to change that to a finite range from 0 to 1.
Also, most of the area under the function curve is concentrate under a peak and becomes neglegible far from it, so we need to focus our calculation around this region.
To deal with this problems, the following change of variables is done:
$$ z = \frac{x}{x + a - 1} $$
This will change the range to $[0,1]$ and place the peak in the middle of this interval, i.e. $z = \frac{1}{2}$.
But there is one last problem that must be dealt: the factor $x^{a-1}$ can become very large and the factor $e^{-x}$ can become very small, and these can cause overflow or underflow. To deal with this, we will write the inegrand as $x^{a-1}e^{-x} = e^{(a-1)\log{x} - x}$.
```diff
- Colocar o método de integração utilizado.
- Falar sobre resultados.
- Colocar imagem da função gama.
```

