from sympy.solvers import solve
from sympy import Symbol
import numpy as np

from values import n_fg, x_H2O, x_CO2, n_H2O_ls
from values import n_ls_dry, m_ls_dry
from values import weights_psd, radii_psd, w1, w2, w3, r1, r2, r3
from values import r_kiln
from problem1 import mass_coal

### ODE ###

def dXdt(R, X, h_p, T_c):
    
    ### FILL IN FROM PROBLEM ###
    return 0

def T_c_drying(P_H2O):
    # The core temperature T_c is a function of
    # P_H2O in the flue gas
    
    # Antoine's equation: P_H2O = 10^(A - B/(C+T_C))
    # [P_H2O] = bar, [T] = K
    # From NIST database:
    A = 3.55959
    B = 643.748
    C = -198.043
    
    T = Symbol('T')
    
    T_c = solve(np.log10(P_H2O) - (A - B/(T+C)), T)[0]

    return T_c

def P_H2O(y_H2O):
    # Calculates partial pressure of H2O in the flue gas
    # y_H2O is the molar fraction of H2O in the flue gas
    # Assuming total pressure of flue gas is 1 bar
    P_tot = 1  # [bar]

    return y_H2O * P_tot

def y_H2O(X):
    # Calculate molar fraction of H2O in the flue gas
    # X is the particle conversion

    n_H2O_fg_in = n_fg * mass_coal * x_H2O
    n_fg_in     = n_fg * mass_coal
    n_CO2_gen   = n_ls_dry

    return (n_H2O_fg_in + (1-X)*n_H2O_ls)/(n_fg_in + n_CO2_gen + (1-X)*n_H2O_ls)


def T_c_calcination(P_CO2):
    # The core temperature T_c is a function of 
    # the partial pressure of CO2 in the flue gas, P_CO2
    
    # Baker, 1962: log10(P_CO2) = -8308/T + 7.079
    # [P_CO2] = 1atm, [T] = K

    # P_CO2 is provided in bar, converting to atm:
    P_CO2_mod = P_CO2 / 1.0135

    T = Symbol('T')
    T_c = solve(np.log10(P_CO2_mod) + 8308/T -7.079, T)

    return T_c

def P_CO2(y_CO2):
    # Calculates partial pressure of CO2 in the flue gas
    # y_H2O is the molar fraction of CO2 in the flue gas
    # Assuming total pressure of flue gas is 1 bar

    P_tot = 1   # [K]

    return y_CO2 * P_tot

def y_CO2(X):
    # Calculate molar fraction of CO2 in the flue gas
    # X is the particle conversion

    n_CO2_fg_in = n_fg * mass_coal * x_CO2
    n_fg_in     = n_fg * mass_coal

    return (n_CO2_fg_in + (1-X)*n_ls_dry)/(n_fg_in + (1-X)*n_ls_dry)

def h_p(X):
    
    G = 1 ### WHAT IS G??? Is the gas-mass-velocity
    h_w = 23.7 * G^(0.67)

    A_particles_not_converted = 0
    
    density_ls = 1 ### MUST BE CHECKED!!!
    H = 1 # HOW TO EXPRESS THIS???

    L = 1 ## WHAT TO DO WITH THIS

    for i in range(3):
        A_particles_not_converted += weights_psd[i]*m_ls_dry/(density_ls*4/3*np.pi*radii_psd[i]**3)*4*np.pi*radii_psd[i]**2 * H

    A_kilnwall = 2*np.pi*r_kiln*L

    hp = h_w * A_kilnwall / A_particles_not_converted

    return hp



