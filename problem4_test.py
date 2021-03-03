from sympy.solvers import solve
from sympy import Symbol

from scipy.integrate import odeint

from numpy import pi
import numpy as np

from values import n_fg, x_H2O_in, x_CO2_in, n_H2O_ls
from values import m_ls_dry, n_ls_dry_pure, n_CO2_gen, density_ls
from values import weights_psd, radii_psd, w1, w2, w3, r1, r2, r3
from values import r_kiln, N, S
from values import Mm_CO2, Mm_H2O, Mm_CO2, Mm_N2, Mm_SO2, Mm_NO, Mm_Cl2, Mm_O2, Mm_ls
from values import x_CO2_in, x_N2_in, x_SO2_in, x_NO_in, x_Cl2_in, x_H2O_in, x_O2_in
from values import T_g_calcination

from values import lamda_cond, deltaH_rxn

from problem1 import mass_coal

### ODE ###

def dXdt(hp, Tc, r, X):
    num = (3*hp*lamda_cond*(T_g_calcination - Tc))
    den = (-deltaH_rxn*density_ls/Mm_ls *r*(lamda_cond + hp*r*(1/(X-1)**(1/3)-1)))
    return num / den

def model(X_c, t):

    X1_c = X_c[0]
    X2_c = X_c[1]
    X3_c = X_c[2]

    hp = h_p_calcination(X1_c, X2_c, X3_c, t)

    Tc = T_c_calcination(P_CO2(y_CO2(X1_c, X2_c, X3_c)))

    dX1dt = dXdt(hp, Tc, r1, X1_c)
    dX2dt = dXdt(hp, Tc, r2, X2_c)
    dX3dt = dXdt(hp, Tc, r3, X3_c)
    
    return [dX1dt, dX2dt, dX3dt]


def T_c_calcination(P_CO2):
    # The core temperature T_c is a function of 
    # the partial pressure of CO2 in the flue gas, P_CO2
    
    # Baker, 1962: log10(P_CO2) = -8308/T + 7.079
    # [P_CO2] = 1atm, [T] = K

    T = Symbol('T')
    T_c = solve(np.log10(float(P_CO2)) + 8308/T -7.079, T)

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


n = 101
time_points = np.linspace(0, 100, n)

initial = [0, 0, 0]

store_sol_1 = np.empty_like(time_points)
store_sol_2 = np.empty_like(time_points)
store_sol_3 = np.empty_like(time_points)

store_sol_1[0] = 0
store_sol_2[0] = 0
store_sol_3[0] = 0

for i in range(1, n):
    tspan = [time_points[i-1], time_points[i]]

    z = odeint(model, initial, tspan)

    store_sol_1[i] = z[1][0]
    store_sol_2[i] = z[1][1]
    store_sol_3[i] = z[1][2]

    initial = z[1]

print(store_sol_1)




