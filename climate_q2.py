import matplotlib.pyplot as plt
import pandas as pd
mapdata = pd.read_csv(r".\climate.csv")

years = mapdata['Year']
co2 = mapdata['CO2']
temp = mapdata['Temperature']

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.savefig("co2_temp_2.png")
plt.show()