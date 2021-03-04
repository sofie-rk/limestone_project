# Plot results from the sensitivity analysis

import matplotlib.pyplot as plt

# Y-labels
ylabel_time = "Total residence time [s]"
ylabel_length = "Length of the kiln [m]"
ylabel_mc = "Mass of coal [tonnes/year]"

# Labels
label_time = "Total residence time"
label_length = "Length of the kiln"
label_mc = "Mass of coal"

# Genereal code for making plot of residence time, length and mass of coal
def generate_3plots(variation, time, length, mc, xlabel):
    plt.subplot(3, 1, 1)
    plt.plot(variation, time, "o-", label=label_time, color="red")
    plt.ylabel(ylabel_time)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(variation, length, "o-", label=label_length, color="blue")
    plt.ylabel(ylabel_length)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(variation, mc, "o-", label=label_mc, color="green")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel_mc)
    plt.legend(loc="lower right")

    plt.show()


# General plot for making a single plot
def generate_1plot(xaxis, yaxis, xlabel, ylabel, plotlabel):

    plt.plot(xaxis, yaxis, "o-", label=plotlabel, color="blue")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

# CHANGING TEMPERATURE OF FLUE GAS OUT OF THE REACTOR
temperatures = [200, 300, 400, 500, 600]
time_temp = [30350, 28830, 27110, 25490, 23870]
length_temp = [139.52, 132.56, 124.63, 117.18, 109.74]
mc_temp = [8552, 9289, 10146, 11155, 12366]

generate_3plots(temperatures, time_temp, length_temp, mc_temp, "Temperature of flue gas out of the kiln [$^oC$]")


# CHANGING HEAT LOSS 
heat_loss = [0, 10, 20, 30, 40]
time_heatloss = [26250, 24150, 22050, 19650]
length_heatloss = [120.68, 111, 101.37, 90]
mc_heatloss = [9289, 10496, 12064, 14183, 17205]

generate_1plot(heat_loss, mc_heatloss, "Heat loss [%]", ylabel_mc, label_mc)

# CHANGING DIAMETER
diameters = [2, 3, 4, 5]
time_dia = [38130, 28830, 23500, 20170]
length_dia = [116.86, 132.56, 144.05, 154.54]
mc_dia = [9289, 9289, 9289, 9289]

generate_3plots(diameters, time_dia, length_dia, mc_dia, "Diameter of the kiln [m]")

# CHANGING ROTATIONS
rotations = [0.2, 0.33333, 0.4, 0.5]
time_rot = [49150, 28830, 23750, 18800]
length_rot = [135.57, 132.56, 131.02, 129.64]
mc_rot = [9289, 9289, 9289, 9289]

generate_3plots(rotations, time_rot, length_rot, mc_rot, "Rotations per minute")
