from values import x_CO2_in, x_N2_in, x_SO2_in, x_NO_in, x_Cl2_in, x_H2O_in, x_O2_in
from values import n_fg, n_H2O_ls, n_CO2_gen
from problem1 import mass_coal


### CALCULATING AMOUNT OF FLUEGAS AT THE ENTRY BASED ON TABLE 3 ###
n_CO2_in    = x_CO2_in     * n_fg * mass_coal
n_N2_in     = x_N2_in      * n_fg * mass_coal
n_SO2_in    = x_SO2_in     * n_fg * mass_coal
n_NO_in     = x_NO_in      * n_fg * mass_coal
n_Cl2_in    = x_Cl2_in     * n_fg * mass_coal
n_H2O_in    = x_H2O_in     * n_fg * mass_coal
n_O2_in     = x_O2_in      * n_fg * mass_coal

### H2O vapor is generated from evaporation of water in the wet limestone ###
n_H2O_gen = n_H2O_ls

### CALCULATING AMOUNT OF FLUE GAS AT THE EXIT ###
n_CO2_out   = n_CO2_in + n_CO2_gen
n_N2_out    = n_N2_in
n_SO2_out   = n_SO2_in
n_NO_out    = n_NO_in
n_Cl2_out   = n_Cl2_in
n_H2O_out   = n_H2O_in + n_H2O_gen
n_O2_out    = n_O2_in 

n_fg_out = n_CO2_out + n_N2_out + n_SO2_out + n_NO_out + n_Cl2_out + n_H2O_out + n_O2_out

### CALCULATING MOLE FRACTIONS (COMPOSITION) AT THE EXIT ###
x_CO2_out   = n_CO2_out / n_fg_out
x_N2_out    = n_N2_out  / n_fg_out
x_SO2_out   = n_SO2_out / n_fg_out
x_NO_out    = n_NO_out  / n_fg_out
x_Cl2_out   = n_Cl2_out / n_fg_out
x_H2O_out   = n_H2O_out / n_fg_out
x_O2_out    = n_O2_out  / n_fg_out

### VERIFYING THAT THE MOLE FRACTIONS ADD UP TO 1 ###
x_sum_out = x_CO2_out + x_N2_out + x_SO2_out + x_NO_out + x_Cl2_out + x_H2O_out + x_O2_out


### PRINTING THE RESULT ###
print("\nCOMPOSITION AT THE EXIT OF THE KILN\n")
print('{0:10} {1:15} {2:15} {3:10}'.format("", "Mol", "Mole fraction", "Percentage"))
print('{0:10} {1:<15.0f} {2:<15.3f} {3:<10.1f}'.format("CO2", n_CO2_out, x_CO2_out, x_CO2_out*100))
print('{0:10} {1:<15.0f} {2:<15.3f} {3:<10.1f}'.format("N2", n_N2_out, x_N2_out, x_N2_out*100))
print('{0:10} {1:<15.0f} {2:<15.3f} {3:<10.1f}'.format("SO2", n_SO2_out, x_SO2_out, x_SO2_out*100))
print('{0:10} {1:<15.0f} {2:<15.3f} {3:<10.1f}'.format("NO", n_NO_out, x_NO_out, x_NO_out*100))
print('{0:10} {1:<15.0f} {2:<15.5f} {3:<10.3f}'.format("Cl2", n_Cl2_out, x_Cl2_out, x_Cl2_out*100))
print('{0:10} {1:<15.0f} {2:<15.3f} {3:<10.1f}'.format("H2O", n_H2O_out, x_H2O_out, x_H2O_out*100))
print('{0:10} {1:<15.0f} {2:<15.3f} {3:<10.1f}'.format("O2", n_O2_out, x_O2_out, x_O2_out*100))
