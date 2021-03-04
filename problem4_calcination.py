# numpy makes math in python easier
import numpy as np
from numpy import pi

# matplotlib.pyplot is used for plotting
import matplotlib.pyplot as plt

# scipy.integrate.odeint is used for solving ODE
from scipy.integrate import odeint

# sympy.solvers.solve is used to solve equations for Tc
from sympy.solvers import solve
from sympy import Symbol

# importing necessary values from other files
from values import r1, r2, r3, w1, w2, w3
from values import deltaH_rxn
from values import density_ls, Mm_ls, lamda_cond, lamda_lime, Mm_CO2
from values import T_g_calcination
from values import n_fg, x_CO2_in, n_ls_dry_pure, m_ls_dry_pure
from values import r_kiln, d_kiln, N, S
from values import m_fg_in_per_m_c
from values import seconds_in_a_year, minutes_in_a_year
from problem1 import mass_coal



def dXdt(r, X, Tc, hp):

    num = 3*hp*lamda_lime*(T_g_calcination-Tc)

    if (X-1 < 0):
        den = deltaH_rxn*density_ls/Mm_ls * r*(lamda_lime + hp*r*(1/((-1)*(1-X)**(float(1/3))-1)) )
    else:
        den = deltaH_rxn*density_ls/Mm_ls * r*(lamda_lime + hp*r*(1/((X-1)**(float(1/3))-1)))

    #print(num/den)

    return num/den


def T_c_calcination(X1_c, X2_c, X3_c):

    # CALCULATING y_CO2
    n_CO2_fg_in = n_fg * mass_coal * x_CO2_in
    n_fg_in     = n_fg * mass_coal

    n_CO2_c = ((1-X1_c)*w1 + (1-X2_c)*w2 + (1-X3_c)*w3)*n_ls_dry_pure
    
    y_CO2 = (n_CO2_fg_in + n_CO2_c)/(n_fg_in + n_CO2_c)

    ### CALCULATING p_CO2
    P_CO2 = y_CO2 * 1 # [atm], p_tot = 1atm

    #print("PCO2: ", P_CO2)

    ### CALCULATING T_c from Baker
    T = Symbol('T')
    T_c = solve(np.log10(float(P_CO2)) + 8308/T -7.079, T)[0]

    #print("Tc: ", T_c)

    return T_c



def h_p_calcination(X1_c, X2_c, X3_c):

    G = m_fg_in_per_m_c*mass_coal/seconds_in_a_year
    G += w1*(1-X1_c)*n_ls_dry_pure*Mm_CO2/seconds_in_a_year 
    G += w2*(1-X2_c)*n_ls_dry_pure*Mm_CO2/seconds_in_a_year
    G += w3*(1-X3_c)*n_ls_dry_pure*Mm_CO2/seconds_in_a_year
    G = G/(pi*r_kiln**2)

    #print(G)

    hw = 23.7*G**(0.67)

    A_kiln_wall = 2*pi*r_kiln* (N*d_kiln*S)/0.19

    A_particle = 0
    if X1_c < 1:
        A_particle += w1 * m_ls_dry_pure/(minutes_in_a_year) * 3 /(density_ls*r1)
    if X2_c < 1:
        A_particle += w2 * m_ls_dry_pure/(minutes_in_a_year) * 3/(density_ls*r2)
    if X3_c < 1:
        A_particle += w3 * m_ls_dry_pure/(minutes_in_a_year) * 3/(density_ls*r3)

    
    if A_particle == 0:
        hp = 0

    else:
        hp = hw * A_kiln_wall/A_particle

    #print(hp)

    return hp



def model(X, t):
    X1_c = X[0]
    X2_c = X[1]
    X3_c = X[2]

    # Find Tc and hp (functions of X1_c, X2_c, X3_c)
    Tc = T_c_calcination(X1_c, X2_c, X3_c)
    hp = h_p_calcination(X1_c, X2_c, X3_c)

    # Find expressions for ODES
    dX1dt = dXdt(r1, X1_c, Tc, hp)
    dX2dt = dXdt(r2, X2_c, Tc, hp)
    dX3dt = dXdt(r3, X3_c, Tc, hp)

    return [dX1dt, dX2dt, dX3dt]

# INITIAL CONDITIONS
X_0 = [0.0, 0.0, 0.0]

# Number of timepoints
n = 21

# Time points
t = np.linspace(0, 30000, n)

# Store solution
X1_c_store = np.empty_like(t)
X2_c_store = np.empty_like(t)
X3_c_store = np.empty_like(t)

# Add initial condition to stored solution
X1_c_store[0] = X_0[0]
X2_c_store[0] = X_0[1]
X3_c_store[0] = X_0[2]

### SOLVING ODE ###
for i in range(1, n):
    tspan = [t[i-1], t[i]] 

    X = odeint(model, X_0, tspan)  # scipy.integrate.odeint

    # Correct if
    if X[1][0] > 1:
        X[1][0] = 1
    if X[1][1] > 1:
        X[1][1] = 1
    if X[1][2] > 1:
        X[1][2] = 1

    # Store obtained values i
    X1_c_store[i] = X[1][0]
    X2_c_store[i] = X[1][1]
    X3_c_store[i] = X[1][2]

    # Give new initial conditions
    X_0 = X[1]

plt.plot(t, X1_c_store, "o", label="X1_c")
plt.plot(t, X2_c_store, "o", label="X2_c")
plt.plot(t, X3_c_store, "o", label="X3_c")
plt.legend()
plt.title("CALCINATION")
plt.xlabel("Time t [s]")
plt.ylabel("Conversion X")
plt.show()

### FINDING RESIDENCE TIMES ###


tau3_c = 0 

for i in range(len(X3_c_store)):
    print(X3_c_store[i])
    if X3_c_store[i] == 1:
        tau3_c = t[i]
        break

print("Residence time calcination: ", tau3_c)
print("SCRIPT problem4_calcination.py IS DONE")




