from numpy import pi, tan
### ABBREVATIONS USED IN CODE ###
# fg:   flue gas
# ls:   limestone (CaCO3)

### TEMPERATURES ###
T_limestone     = 25 + 273      # [K]
T_fg_in         = 25 + 273      # [K] 
T_fg_out        = 300 + 273     # [K]
T_H2O_boil      = 100 + 273     # [K]
T_g_calcination = 1100 + 273    # [K]
T_g_drying      = 300 + 273     # [K]

### MOLAR MASSES [kg/mol] ###
Mm_ls   = 100   * 10**(-3)      
Mm_H2O  = 18.02 * 10**(-3) 
Mm_CO2  = 44.01 * 10**(-3)
Mm_N2   = 28.05 * 10**(-3)
Mm_SO2  = 64.06 * 10**(-3)
Mm_NO   = 30.01 * 10**(-3)
Mm_Cl2  = 70.90 * 10**(-3)
Mm_O2   = 32.00 * 10**(-3)


### LIMESTONE CONDITIONS ###
m_ls_wet = 115000 * 1000            # [kg/year] wet limestone
w_H2O_ls = 7/100                    # [-] weight percent H2O in limestone

m_ls_dry = m_ls_wet * (1-w_H2O_ls)  # [kg/year] mass dry limestone
m_H2O_ls = m_ls_wet * w_H2O_ls      # [kg/year] mass H2O in wet limestone
n_H2O_ls = m_H2O_ls / Mm_H2O                        # [mol/year] H2O in wet limestone

m_CO2_gen = m_ls_dry * 0.436        # [kg/year] 43.6% of limestone mass is lost as CO2
n_CO2_gen = m_CO2_gen / Mm_CO2      # [mol/year] CO2 generated in calcination reaction

purity_ls = 0.987                                   # [-] weight fraction pure limestone
m_ls_dry_pure = m_ls_dry * purity_ls                # [kg/year] pure and dry CaCO3
n_ls_dry_pure = m_ls_dry * purity_ls / Mm_ls        # [mol/year] pure and dry CaCO3 

density_ls = 2.8*1000               # [kg/m^3] CHECK THIS OUT!!!
lamda_cond = 1.33                   # [J/s m K] conductivity lime
lamda_lime = 0.8                   # [J/s mK]

### ENTHALPIES ###
deltaH_rxn = 183*10**3          # [J/mol] CaCO3, @25C
deltaH_evap = 40660             # [J/mol] !!!!CHECK THIS

### OTHER VALUES ###
n_fg = 426                  # [mol/kg coal] mole of flue gas generated per kg coal combusted
LHV_coal = 28.4 * 10**6     # [J/kg coal] heating value of coal

### MOLE FRACTION COMPOSITION OF FLUE GAS AT THE ENTRY ###
x_CO2_in = 14.4/100
x_N2_in = 75.3/100
x_SO2_in = 0.1/100
x_NO_in = 0.3/100
x_Cl2_in = 0.001/100
x_H2O_in = 6.6/100
x_O2_in = 3.3/100

m_fg_in_per_m_c = (x_CO2_in*Mm_CO2 + x_N2_in*Mm_N2 + x_SO2_in*Mm_SO2 + x_NO_in*Mm_NO + \
                    x_Cl2_in*Mm_Cl2 + x_H2O_in*Mm_H2O + x_O2_in*Mm_O2) * n_fg



### KILN ###
d_kiln = 3          # [m]
r_kiln = d_kiln/2   # [m]
N = (1/3)             # rotations per seoncd (1/3 per minute)
S = tan(3*pi/180)           # inclination in ft pr ft



### PARTICLE SIZE DISTRIBUTION OF FAXE BRYOZO ###
w1 = 27 / 100               # [-]
w2 = 40 / 100               # [-]
w3 = 33 / 100               # [-]
weights_psd = [w1, w2, w3]
d1 = (8+6)/2    * 10**(-3)  # [m] MEAN DIAMETER SIZE 1
d2 = (25+27)/2  * 10**(-3)  # [m] MEAN DIAMETER SIZE 2
d3 = (44+46)/2  * 10**(-3)  # [m] MEAN DIAMATER SIZE 3
diameters_psd = [d1, d2, d3]
r1 = d1/2                   # [m] mean radius size 1
r2 = d2/2                   # [m] mean radius size 2
r3 = d3/2                   # [m] mean radius size 3
radii_psd = [r1, r2, r3]  


seconds_in_a_year = 60*60*24*365
minutes_in_a_year = 60*24*365

