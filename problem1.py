from values import *
from heat_capacities import *

from sympy.abc import x
from sympy import integrate


### HEAT REQUIRED IN THE REACTION ###
Q_reaction = deltaH_rxn * n_ls_dry

### HEAT REQUIRED TO EVAPORATE WATER IN THE LIMESTONE ###

# Heat water liquid from 25C in to 100C (boiling point)
Q_heat_w_liq = integrate(cp(A_w_l, B_w_l, C_w_l, D_w_l, E_w_l, x), (x, T_fg_in/1000, T_H2O_boil/1000))

# Heat water gas from 100C to 300C (flue gas outlet temperature)
Q_heat_w_gas = integrate(cp(A_w_g, B_w_g, C_w_g, D_w_g, E_w_g, x), (x, T_H2O_boil/1000, T_fg_out/1000))


Q_evaporation = (Q_heat_w_liq + deltaH_evap + Q_heat_w_gas) * n_H2O_ls


### HEAT REQUIRED TO HEAT THE FLUE GAS TO 300C ###

# CO2 produced in reaction must be heated from 25C til 300C
# 1 mol CaCO3 reacted gives 1 mol CO2
n_CO2_formed = n_ls_dry

Q_CO2 = n_CO2_formed * integrate(cp(A_CO2, B_CO2, C_CO2, D_CO2, E_CO2, x), (x, T_fg_in/1000, T_fg_out/1000))

# Need to heat the flue gas from 25C to 300C
Q_fg = integrate(   x_CO2 * cp(A_CO2, B_CO2, C_CO2, D_CO2, E_CO2, x) + \
                    x_N2 * cp(A_N2, B_N2, C_N2, D_N2, E_N2, x) + \
                    x_SO2 * cp(A_SO2, B_SO2, C_SO2, D_SO2, E_SO2, x) + \
                    x_NO * cp(A_NO, B_NO, C_NO, D_NO, E_NO, x) + \
                    x_Cl2 * cp(A_Cl2, B_Cl2, C_Cl2, D_Cl2, E_Cl2, x) + \
                    x_H2O * cp(A_w_g, B_w_g, C_w_g, D_w_g, E_w_g, x) + \
                    x_O2 * cp(A_O2, B_O2, C_O2, D_O2, E_O2, x)
                        , (x, T_fg_in/1000, T_fg_out/1000))



### HEAT LOSS TO THE ENVIRONMENT ###

Q_heat_loss = 0


### ENERGY BALANCE ###

# LHV * mass_coal = Q_evaporation + Q_reaction + Q_heat_loss + Q_CO2 + Q_fl*n_fg*mass_coal

mass_coal = (Q_evaporation + Q_reaction + Q_CO2 + Q_heat_loss) / (LHV_coal - Q_fg*n_fg)


print("Q flue gas: " , Q_fg)
print("Q reaction: ", Q_reaction)
print("Q evaporation: ", Q_evaporation)

print("MASS COAL: ", mass_coal)