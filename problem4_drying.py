import numpy as np
from numpy import pi

import matplotlib.pyplot as plt

from scipy.integrate import odeint

from sympy.solvers import solve
from sympy import Symbol

from problem1 import mass_coal

#from problem4_calcination import tau1_c, tau2_c, tau3_c
from values import deltaH_evap, w_H2O_ls
from values import lamda_cond, T_g_drying 
from values import m_ls_dry_pure, density_ls
from values import Mm_H2O, Mm_CO2
from values import n_fg, x_H2O_in
from values import w1, w2, w3, r1, r2, r3
from values import n_H2O_ls, n_CO2_gen
from values import seconds_in_a_year, minutes_in_a_year
from values import m_fg_in_per_m_c
from values import r_kiln, N, S, d_kiln

def dXdt(r, X, Tc, hp):

    num = 3*hp*lamda_cond*(T_g_drying-Tc)

    if (X-1 < 0):
        den = deltaH_evap*density_ls/Mm_H2O * w_H2O_ls/(1-w_H2O_ls) * r*(lamda_cond + hp*r*(1/((-1)*(1-X)**(float(1/3))-1)) )
    else:
        den = deltaH_evap*density_ls/Mm_H2O * r*(lamda_cond + hp*r*(1/((X-1)**(float(1/3))-1)))

    return num/den

def T_c_drying(X1_d, X2_d, X3_d):

    # Calculating y_H2O
    n_H2O_fg_in = n_fg * mass_coal * x_H2O_in
    n_fg_in     = n_fg * mass_coal

    n_H2O_d = ((1-X1_d)*w1 + (1-X2_d)*w2 + (1-X3_d)*w3) * n_H2O_ls

    y_H2O = (n_H2O_fg_in + n_H2O_d)/(n_fg_in + n_CO2_gen + n_H2O_d)

    # Calculating p_H2O
    P_H2O = y_H2O * 1.0135 # [bar], p_tot = 1atm

    # Calculating T_c using Antoine's equation
    # Antoine's equation: P_H2O = 10^(A - B/(C+T_C))
    # [P_H2O] = bar, [T] = K
    # From NIST database:
    A = 3.55959
    B = 643.748
    C = -198.043
    
    T = Symbol('T')

    T_c = solve(np.log10(float(P_H2O)) - (A - B/(T+C)), T)

    return T_c[0]

def h_p_drying(X1_d, X2_d, X3_d):

    G = m_fg_in_per_m_c*mass_coal/seconds_in_a_year
    G += w1*(1-X1_d)*n_H2O_ls*Mm_H2O/seconds_in_a_year 
    G += w2*(1-X2_d)*n_H2O_ls*Mm_H2O/seconds_in_a_year
    G += w3*(1-X3_d)*n_H2O_ls*Mm_H2O/seconds_in_a_year
    G += n_CO2_gen*Mm_CO2/seconds_in_a_year
    G = G/(pi*r_kiln**2)

    #print(G)

    hw = 23.7*G**(0.67)

    A_kiln_wall = 2*pi*r_kiln* (N*d_kiln*S)/0.19

    A_particle = 0
    if X1_d < 1:
        A_particle += w1 * m_ls_dry_pure/(minutes_in_a_year) * 3 /(density_ls*r1)
    if X2_d < 1:
        A_particle += w2 * m_ls_dry_pure/(minutes_in_a_year) * 3/(density_ls*r2)
    if X3_d < 1:
        A_particle += w3 * m_ls_dry_pure/(minutes_in_a_year) * 3/(density_ls*r3)

    
    if A_particle == 0:
        hp = 0

    else:
        hp = hw * A_kiln_wall/A_particle

    #print(hp)

    return hp


def model_drying(X, t):
    X1_d = X[0]
    X2_d = X[1]
    X3_d = X[2]

    # Find Tc and hp (functions of X1_d, X2_d, X3_d)
    Tc = T_c_drying(X1_d, X2_d, X3_d)
    hp = h_p_drying(X1_d, X2_d, X3_d)

    # Find expressions for ODES
    dX1dt = dXdt(r1, X1_d, Tc, hp)
    dX2dt = dXdt(r2, X2_d, Tc, hp)
    dX3dt = dXdt(r3, X3_d, Tc, hp)

    return [dX1dt, dX2dt, dX3dt]

# INITIAL CONDITIONS
X_0_drying = [0, 0, 0]

# Number of timepoints
n = 201

# Time points
t = np.linspace(0, 3000, n)

# Store solution
X1_d_store = np.empty_like(t)
X2_d_store = np.empty_like(t)
X3_d_store = np.empty_like(t)

# Add initial condition to stored solution
X1_d_store[0] = X_0_drying[0]
X2_d_store[0] = X_0_drying[1]
X3_d_store[0] = X_0_drying[2]

### SOLVING ODE ###
for i in range(1, n):
    tspan = [t[i-1], t[i]] 
    
    X = odeint(model_drying, X_0_drying, tspan)  # scipy.integrate.odeint

    # Correct if
    if X[1][0] > 1:
        X[1][0] = 1
    if X[1][1] > 1:
        X[1][1] = 1
    if X[1][2] > 1:
        X[1][2] = 1

    # print(X[1][0])
    # print(X[1][1])
    # print(X[1][2])
    # Store obtained values i
    X1_d_store[i] = X[1][0]
    X2_d_store[i] = X[1][1]
    X3_d_store[i] = X[1][2]

    # Give new initial conditions
    X_0_drying = X[1]


plt.plot(t, X1_d_store, label="X1_d")
plt.plot(t, X2_d_store, label="X2_d")
plt.plot(t, X3_d_store, label="X3_d")
plt.legend()
plt.title("DRYING")
plt.xlabel("Time t [s]")
plt.ylabel("Conversion X")
plt.show()

tau3_d = 0
for i in range(len(X3_d_store)):
    if X3_d_store[i] == 1:
        tau3_d = t[i]
        break

print("Residence time drying: ", tau3_d)
print("SCRIPT problem4_drying.py IS DONE")