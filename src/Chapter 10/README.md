# Chapter 10:

## Exercise 10.9:
The <b>Ising model</b> is a theoretical model to describe the magnetization of a material. It considers that the material is made up of magnetic dipoles (spins) that can interact with each other and with an external magnetic field. In this exercise, I performed a <b>Markov chain Monte Carlo simulation</b> of the Ising model on a square lattice of 20x20 spins. In each step of the simulation, I sorted a spin to flip its sign and calculate the energy difference. Then, I used a <b>Metropolis-style algorithm</b> to decide if the transition should be accepted. With this program, it was possible to make plots of the evolution of the energy and magnetization of the system. After some time, the system reaches an equilibrium situation. For instance, the evolution of the magnetization in a run of the algorithm with one million steps can be seen below:
```diff
-colocar imagem
```
I also made an animation of the evolution of the spin-lattice using the <b>vpython</b> library. In it, red circles represent spins with value +1, while green circles represent spins with value -1. With these simulations, it was possible to note a phase transition of the system above some temperature. There was a spontaneous magnetization for low temperatures, while for high temperatures, the mean magnetization was zero. Below, there are three frames of the animation, each one for a different temperature.
```diff
- colocar imagens
```
