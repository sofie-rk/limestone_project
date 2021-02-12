### ABBREVATIONS USED IN CODE ###
# fg:   flue gas
# ls:   limestone (CaCO3)




### TEMPERATURES ###
T_limestone = 25 + 273  # [K]
T_fg_in = 25 + 273      # [K] 
T_fg_out = 300 + 273    # [K]
T_H2O_boil = 100 + 273    # [K]

### MOLAR MASSES [kg/mol] ###
Mm_ls = 100*10**(-3)      
Mm_H2O = 18.02*10**(-3) 

### INITIAL CONDITIONS ###
m_ls_wet = 115000 * 1000            # [kg] wet limestone
w_H2O_ls = 0.07                     # [-] weight percent H2O in limestone

m_ls_dry = m_ls_wet * (1-w_H2O_ls)  # [kg] mass dry limestone
m_H2O_ls = m_ls_wet * w_H2O_ls      # [kg] mass H2O in wet limestone

n_ls_dry = m_ls_dry / Mm_ls         # [mol] mol dry limestone
n_H2O_ls = m_H2O_ls / Mm_H2O        # [mol] mol H2O in wet limestone

### ENTHALPIES ###
deltaH_rxn = 183        # [kJ/mol] limestone, @25C

### OTHER VALUES ###
deltaH_evap = 2256.4    # [kJ/kg] !!!!CHECK THIS
n_fg = 426              # [mol/kg coal] mole of flue gas generated per kg coal combusted
LHV_coal = 28.4 * 10**3 # [kJ/kg coal] heating value of coal

### MOLE FRACTION COMPOSITION OF FLUE GAS AT THE ENTRY ###
x_CO2 = 14.4/100
x_N2 = 75.3/100
x_SO2 = 0.1/100
x_NO = 0.3
x_Cl2 = 0.001/100
x_H2O = 6.6/100
x_O2 = 3.3/100


