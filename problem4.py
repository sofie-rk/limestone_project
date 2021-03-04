from sympy.solvers import solve
from sympy import Symbol
from numpy import pi
import numpy as np

from values import n_fg, x_H2O_in, x_CO2_in, n_H2O_ls
from values import m_ls_dry, n_ls_dry_pure, n_CO2_gen, density_ls
from values import weights_psd, radii_psd, w1, w2, w3, r1, r2, r3
from values import r_kiln, N, S
from values import Mm_CO2, Mm_H2O, Mm_CO2, Mm_N2, Mm_SO2, Mm_NO, Mm_Cl2, Mm_O2
from values import x_CO2_in, x_N2_in, x_SO2_in, x_NO_in, x_Cl2_in, x_H2O_in, x_O2_in
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

    # Convert from atm to bar
    P_H2O_mod = P_H2O * 1.0135
    
    T_c = solve(np.log10(P_H2O_mod) - (A - B/(T+C)), T)[0]

    return T_c

def P_H2O(y_H2O):
    # Calculates partial pressure of H2O in the flue gas
    # y_H2O is the molar fraction of H2O in the flue gas
    # Assuming total pressure of flue gas is 1 atm
    P_tot = 1  # [atm]

    return y_H2O * P_tot

def y_H2O(X1_d, X2_d, X3_d):
    # Calculate molar fraction of H2O in the flue gas
    # X is the particle conversion

    n_H2O_fg_in = n_fg * mass_coal * x_H2O_in
    n_fg_in     = n_fg * mass_coal

    n_H2O_d = ((1-X1_d)*w1 + (1-X2_d)*w2 + (1-X3_d)*w3) * n_H2O_ls

    return (n_H2O_fg_in + n_H2O_d)/(n_fg_in + n_CO2_gen + n_H2O_d)


def T_c_calcination(P_CO2):
    # The core temperature T_c is a function of 
    # the partial pressure of CO2 in the flue gas, P_CO2
    
    # Baker, 1962: log10(P_CO2) = -8308/T + 7.079
    # [P_CO2] = 1atm, [T] = K

    T = Symbol('T')
    T_c = solve(np.log10(P_CO2) + 8308/T -7.079, T)

    return T_c

def P_CO2(y_CO2):
    # Calculates partial pressure of CO2 in the flue gas
    # y_H2O is the molar fraction of CO2 in the flue gas
    # Assuming total pressure of flue gas is 1 bar

    P_tot = 1   # [K]

    return y_CO2 * P_tot

def y_CO2(X1_c, X2_c, X3_c):
    # Calculate molar fraction of CO2 in the flue gas
    # X is the particle conversion

    n_CO2_fg_in = n_fg * mass_coal * x_CO2_in
    n_fg_in     = n_fg * mass_coal

    n_CO2_c = ((1-X1_c)*w1 + (1-X2_c)*w2 + (1-X3_c)*w3)*n_ls_dry_pure

    return (n_CO2_fg_in + n_CO2_c)/(n_fg_in + n_CO2_c)

def h_p_calcination(X1_c, X2_c, X3_c, t):
    # Calculating mass of flue gas in
    m_fg_in = (x_CO2_in/Mm_CO2 + x_N2_in/Mm_N2 + x_SO2_in/Mm_SO2 + x_NO_in/Mm_NO + x_Cl2_in/Mm_Cl2 + x_H2O_in/Mm_H2O + x_O2_in/Mm_O2) * n_fg * Mm_CO2
    
    m_CO2_c = ((1-X1_c)*w1 + (1-X2_c)*w2 + (1-X3_c)*w3)*n_ls_dry_pure / Mm_CO2

    G = (m_fg_in + m_CO2_c) / A_cross_sectional_kiln

    hw = 23.7*G**(0.67)

    A_kiln_wall = 2*pi*r_kiln* (t*N*D_ft*S)/0.19

    A_particle = 0
    if X1_c < 1:
        A_particle += w1*m_ls_dry / (density_ls*r1) * 3
    if X2_c < 1:
        A_particle += w2*m_ls_dry / (density_ls*r2) * 3
    if X3_c < 1:
        A_particle += w1*m_ls_dry / (density_ls*r1) * 3
    
    hp = hw * A_kiln_wall/A_particle

    return hp



    

def h_p_drying(X1_d, X2_d, X3_d):

    # Calculating mass of flue gas in
    m_fg_in = (x_CO2_in/Mm_CO2 + x_N2_in/Mm_N2 + x_SO2_in/Mm_SO2 + x_NO_in/Mm_NO + x_Cl2_in/Mm_Cl2 + x_H2O_in/Mm_H2O + x_O2_in/Mm_O2) * n_fg * Mm_CO2
    
    
    m_H2O_d = ((1-X1_d)*w1 + (1-X2_d)*w2 + (1-X3_d)*w3)*n_H2O_ls / Mm_H2O

    m_CO2_c = n_CO2_gen / Mm_CO2

    crossectional_area = np.pi * r_kiln**2

    G = (m_fg_in + m_CO2_c + m_H2O_d) / crossectional_area # gas-mass-velocity [kg/m^2s]
    
    h_w = 23.7 * G**(0.67)

    A_particles_not_converted = 0
    
    density_ls = 1 ### MUST BE CHECKED!!!
    H = 1 # HOW TO EXPRESS THIS???

    L = 1 ## WHAT TO DO WITH THIS

    for i in range(3):
        A_particles_not_converted += weights_psd[i]*m_ls_dry/(density_ls*4/3*np.pi*radii_psd[i]**3)*4*np.pi*radii_psd[i]**2 * H

    A_kilnwall = 2*np.pi*r_kiln*L

    hp = h_w * A_kilnwall / A_particles_not_converted

    return hp



