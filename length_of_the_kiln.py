#from problem4_calcination import tau3_c
#from problem4_drying import tau3_d

from problem1 import mass_coal

from values import N, S, d_kiln
from values import seconds_in_a_minute


tau3_c = 26100
tau3_d = 2730

total_residence_time = tau3_c + tau3_d

length = ((tau3_c + tau3_d)* N/seconds_in_a_minute *d_kiln*S)/0.19

print("RESIDENCE TIME: ", total_residence_time)
print("LENGTH OF THE KILN: ", length)
print("MASS OF COAL", round(mass_coal/1000))
