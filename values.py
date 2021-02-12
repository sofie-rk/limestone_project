### ABBREVATIONS USED IN CODE ###
# fg:   flue gas
# ls:   limestone (CaCO3)




### TEMPERATURES ###
T_limestone = 25 + 273  # [K]
T_fg_in = 25 + 273      # [K] 
T_fg_out = 300 + 273    # [K]
T_H2O_boil = 100 + 273    # [K]

### REACTION ENTHALPY ###
deltaH_rxn = 183        # [kJ/mol] limestone, @25C

### INITIAL CONDITIONS ###
m_ls_start = 115000 * 1000     # [kg] wet limestone
w_H2O_ls = 0.07                    # weight percent H2O in limestone

### OTHER VALUES ###
Mm_ls = 0.100           # [kg/mol] molar mass CaCO3
Mm_H2O = 18.02*10**(-3) # [kg/mol] molar mass H2O
deltaH_evap = 2256.4    # [kJ/kg] !!!!CHECK THIS

### MOLE FRACTION COMPOSITION OF FLUE GAS AT THE ENTRY ###
x_CO2 = 14.4/100
x_N2 = 75.3/100
x_SO2 = 0.1/100
x_NO = 0.3
x_Cl2 = 0.001/100
x_H2O = 6.6/100
x_O2 = 3.3/100


