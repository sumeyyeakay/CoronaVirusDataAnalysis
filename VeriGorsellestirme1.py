# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 02:58:59 2020

@author: sumeyyeakay
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("covid_19_data.csv")
#veri gorsellesirme
#df.plot()
#plt.show()


#SNO yu silmek icin
df = df.drop("SNo", axis=1)
#df.plot()
#plt.show()

#Turkiye datalari uzerinden

turkiye = df[df["Country/Region"] == "Turkey"]
print(turkiye.columns)
#x ole sayisi y sutunu kurtulan
plt.plot(turkiye.Deaths, turkiye.Recovered, color="red", label= "Turkiyede olen-kurtulan sayilari")
plt.xlabel("Olum Sayisi")
plt.ylabel("Kurtulan Hasta Sayisi")
plt.title("Turkiyedeki Coronavirus Sayisi")
plt.legend()
plt.show()

#noktali sekilde gosterilmesi
df.plot(grid=True,linestyle=":")
plt.show()