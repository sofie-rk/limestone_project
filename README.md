# Limestone project

As part of the course "Industrial Reaction Engineering" spring semester 2021 at DTU, I did a group project about production of lime. The codes used for the process modeling is included in this repository.

Lime (CaO) is one of the most important chemicals produced in Denmark. It has a variety of different industrial applications , such as production of building materials, cement, and removal of sulfur oxides.

## problem1.py
Combusion of coal is used to generate the heat needed for the endothermic reaction, evaporation of water in the pores of CaCO3, and for the heating of the flue gas. This code calculated the amount of coal needed, based on an energy balance of the system.

## problem2.py
Calculates the composition of flue gas at the exit of the kiln.

## problem4_calcination.py and problem4_drying.py
Using a shrinking core model, a model for the conversion X and time t is found (dX/dt = f(X)). This code solves a system of ODE's, and finds the time needed for full conversion (X=1).

## length_of_the_kiln.py
A rotary kiln was design based on the calculated time needed for full conversion.


