from values import *
from heat_capacities import *

from sympy.abc import x
from sympy import integrate


### HEAT REQUIRED IN THE REACTION ###
Q_reaction = deltaH_rxn * m_ls_start*(1-w_H2O_ls)/Mm_ls

### HEAT REQUIRED TO EVAPORATE WATER IN THE LIMESTONE ###

# Heat water liquid from 25C in to 100C (boiling point)
Q_heat_w_liq = integrate(cp(A_w_l, B_w_l, C_w_l, D_w_l, E_w_l, x), (x, T_fg_in/1000, T_H2O_boil/1000))

# Heat water gas from 100C to 300C (flue gas outlet temperature)
Q_heat_w_gas = integrate(cp(A_w_g, B_w_g, C_w_g, D_w_g, E_w_g, x), (x, T_H2O_boil/1000, T_fg_out/1000))


Q_evaporation = (Q_heat_w_liq + deltaH_evap + Q_heat_w_gas) * m_ls_start*w_H2O_ls/Mm_H2O


### HEAT REQUIRED TO HEAT THE FLUE GAS TO 300C ###

# CO2 produced in reaction must be heated from 25C til 300C
# 1 mol CaCO3 reacted gives 1 mol CO2
n_CO2_formed = m_ls_start*(1-w_H2O_ls)/Mm_H2O

Q_CO2 = n_CO2_formed * integrate(cp(A_CO2, B_CO2, C_CO2, D_CO2, E_CO2, x), (x, T_fg_in/1000, T_fg_out/1000))





print("Q reaction: ", Q_reaction)
print("Q evaporation: ", Q_evaporation)