# Bringing it all together
In the last but one exercise we considered a set of non-interacting spins that interacted with an external magnetic field.  Then in the previous exercise we considered a set of interacting spins that were not in the presence of a magnetic field.  In this exercise we will bring it all together by writing a program to calculate the Hamiltonian for a set of interacting spins in a magnetic field.  In particular, we are going to consider the following Hamiltonian:

![](https://render.githubusercontent.com/render/math?math=E-\sum_{i=1}^Ns_is_{i%2B1}-H\sum_{i=1}^Ns_i)

Modify the code in `main.py` so that the function called `hamiltonian` calculates the the quantity defined by the formula above.  Notice that this function takes a list called `spins`, which contains all the spin coordinates, as input as well as a scalar variable called `H` that gives the magnetic field strength.  Further notice that the magnetic field strength, `H`, is given in the units of the strength of coupling between the spins.
