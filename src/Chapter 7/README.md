# Chapter 7 - Fourier transforms

## Exercise 7.4:
In this exercise, I had a file with daily data of the Dow Jones Industrial Average (a measure of average prices on the US stock market) from 2006 to 2010. I performed a **Fast Fourier Transform** on this data (using **numpy's** *rfft* function) and set 90% of the coefficients to zero. Then I performed an **inverse fast Fourier transform** and compared the new set of data with the original one. The result can be seen in the graph below:
```diff
-  Adiconar gráfico. Adicionar legenda e titulo no gráfico.
```
As we can see, the new curve follows the general trend of the original data, but it has lost the details. If we don't need a good resolution of the variation of the data in small periods in our application, then this can be a good method to reduce the amount of data we need to store while keeping the relevant information. In the figure below, we stored only 2% of the Fourier coefficients and set the other 98% to zero:
```diff
- Adicionar gráfico. Colocar legenda e titulo
```
The general trend has been preserved again, but with even less detail compared to the previous case. The amount of information that we would store must be analyzed for each specific application.
