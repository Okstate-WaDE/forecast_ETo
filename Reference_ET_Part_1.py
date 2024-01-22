import math
import numpy as np
import re

elevation = 300
t_max = 40
t_min = 20
t_mean = np.mean([t_max, t_min])
hum_max = 70
hum_min = 50
hum_mean = 60
cloud_cover = 45 


P = 101.3 * ((293-0.0065*elevation)/293) ** 5.26            # Atmospheric pressure
λ = 2.54                                                    # Latent heat of vaporization = 2.450 MJ/kg
γ = (0.665/1000)* P                                         # Psychrometric Constant = 0.065 kPa/⁰C


## Calculating Mean Saturation Vapour Pressure

# Saturation  Vapour Pressure at Max temp
e_tmax = 0.6108*math.exp(17.27*t_max/(t_max+237.3))

# Saturation  Vapour Pressure at Min temp
e_tmin = 0.6108*math.exp(17.27*t_min/(t_min+237.3))

# Taking average of sat vapour pressure at max and min temperature
es = np.mean([e_tmax, e_tmin])

# Calculating Actual Vapour Pressure

regex = '^(0|[1-9]\d*)(\.\d+)?$'

check_max = re.match(regex, str(hum_max))
check_min = re.match(regex, str(hum_min))

if check_max and check_min:
    ea = round(((e_tmin*(hum_max/100)) + (e_tmax*(hum_min/100)))/2, 3)

elif check_max:
    ea = round(e_tmin*(hum_max/100), 3)

else:
    ea = round((hum_mean/100)*np.mean([e_tmax, e_tmin]), 3)

# Determining vapour pressure deficit(es_ea)
 
es_ea = round(es - ea, 3)

## Extraterrestrial Radiation

month  = 
day = 
year = 

# Number of day in the given year (J)

j = int((275 * (month/9) - 30 + day) - 2)

if month <3:
    j = j+2

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    if  month >2:
        j = j + 1



