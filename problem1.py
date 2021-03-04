from values import T_fg_in, T_H2O_boil, T_fg_out
from values import n_H2O_ls, n_CO2_gen, n_ls_dry_pure, n_fg
from values import deltaH_rxn, deltaH_evap, LHV_coal
from values import x_CO2_in, x_N2_in, x_SO2_in, x_NO_in, x_Cl2_in, x_H2O_in, x_O2_in
from heat_capacities import *


from sympy.abc import x
from sympy import integrate


### HEAT REQUIRED IN THE REACTION ###
Q_reaction = deltaH_rxn * n_ls_dry_pure

### HEAT REQUIRED TO EVAPORATE WATER IN THE LIMESTONE ###

# Heat water liquid from 25C in to 100C (boiling point)
Q_heat_w_liq = integrate(cp(A_w_l, B_w_l, C_w_l, D_w_l, E_w_l, x), (x, T_fg_in, T_H2O_boil))

# Heat water gas from 100C to 300C (flue gas outlet temperature)
Q_heat_w_gas = integrate(cp(A_w_g, B_w_g, C_w_g, D_w_g, E_w_g, x), (x, T_H2O_boil, T_fg_out))

# print("Liq: ", Q_heat_w_liq)
# print("Evap: ", deltaH_evap)
# print("Gas: ", Q_heat_w_gas)

Q_evaporation = (Q_heat_w_liq + deltaH_evap + Q_heat_w_gas) * n_H2O_ls


### HEAT REQUIRED TO HEAT THE FLUE GAS TO 300C ###

# CO2 produced in reaction must be heated from 25C til 300C

Q_CO2 = n_CO2_gen * integrate(cp(A_CO2, B_CO2, C_CO2, D_CO2, E_CO2, x), (x, T_fg_in, T_fg_out))

# Need to heat the flue gas from 25C to 300C
Q_fg = integrate(   x_CO2_in * cp(A_CO2, B_CO2, C_CO2, D_CO2, E_CO2, x) + \
                    x_N2_in * cp(A_N2, B_N2, C_N2, D_N2, E_N2, x) + \
                    x_SO2_in * cp(A_SO2, B_SO2, C_SO2, D_SO2, E_SO2, x) + \
                    x_NO_in * cp(A_NO, B_NO, C_NO, D_NO, E_NO, x) + \
                    x_Cl2_in * cp(A_Cl2, B_Cl2, C_Cl2, D_Cl2, E_Cl2, x) + \
                    x_H2O_in * cp(A_w_g, B_w_g, C_w_g, D_w_g, E_w_g, x) + \
                    x_O2_in * cp(A_O2, B_O2, C_O2, D_O2, E_O2, x)
                        , (x, T_fg_in, T_fg_out))



### HEAT LOSS TO THE ENVIRONMENT ###

Q_heat_loss = 0
X = 0



### ENERGY BALANCE ###

# LHV * mass_coal = Q_evaporation + Q_reaction + Q_heat_loss + Q_CO2 + Q_fl*n_fg*mass_coal

mass_coal = (Q_evaporation + Q_reaction + Q_CO2 ) / (LHV_coal - Q_fg*n_fg - X*LHV_coal)

#print("Q flue gas: " , Q_fg*n_fg)
#print("Q reaction + CO2: ", Q_reaction + Q_CO2)

#print("Q evaporation: ", Q_evaporation)

print("MASS COAL: ", round(mass_coal/1000), " tonnes")

### FURTHER CALCULATIONS ###

print("N_fg_tot IN", n_fg*mass_coal)
print("N_fg_tot OUT", n_fg*mass_coal + n_CO2_gen + n_H2O_ls)