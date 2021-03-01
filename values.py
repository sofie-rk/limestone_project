### ABBREVATIONS USED IN CODE ###
# fg:   flue gas
# ls:   limestone (CaCO3)

### TEMPERATURES ###
T_limestone = 25 + 273  # [K]
T_fg_in = 25 + 273      # [K] 
T_fg_out = 300 + 273    # [K]
T_H2O_boil = 100 + 273  # [K]

### MOLAR MASSES [kg/mol] ###
Mm_ls = 100*10**(-3)      
Mm_H2O = 18.02*10**(-3) 

### INITIAL CONDITIONS ###
m_ls_wet = 115000 * 1000            # [kg] wet limestone
w_H2O_ls = 7/100                    # [-] weight percent H2O in limestone

m_ls_dry = m_ls_wet * (1-w_H2O_ls)  # [kg] mass dry limestone
m_H2O_ls = m_ls_wet * w_H2O_ls      # [kg] mass H2O in wet limestone

n_ls_dry = m_ls_dry / Mm_ls         # [mol] mol dry limestone
n_H2O_ls = m_H2O_ls / Mm_H2O        # [mol] mol H2O in wet limestone

### ENTHALPIES ###
deltaH_rxn = 183*10**3          # [J/mol] limestone, @25C
deltaH_evap = 40660             # [J/mol] !!!!CHECK THIS

### OTHER VALUES ###
n_fg = 426                  # [mol/kg coal] mole of flue gas generated per kg coal combusted
LHV_coal = 28.4 * 10**6     # [J/kg coal] heating value of coal

### MOLE FRACTION COMPOSITION OF FLUE GAS AT THE ENTRY ###
x_CO2 = 14.4/100
x_N2 = 75.3/100
x_SO2 = 0.1/100
x_NO = 0.3/100
x_Cl2 = 0.001/100
x_H2O = 6.6/100
x_O2 = 3.3/100


### KILN ###
d_kiln = 3          # [m]
r_kiln = d_kiln/2   # [m]


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


