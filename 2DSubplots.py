# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:23:04 2020

@author: sumeyyeakay
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("covid_19_data.csv")

turkiye = df[df["Country/Region"] == "Turkey"]
italya = df[df["Country/Region"] == "Italy"]


df.plot(subplots=True)
plt.subplot(2,1,1)

plt.plot(turkiye.Deaths, turkiye.Recovered, color="red", label= "Turkiyede olen-kurtulan sayilari")
plt.xlabel("Turkiye Olum Sayisi")
plt.ylabel("Turkiye Kurtulan Hasta Sayisi")

plt.subplot(2,1,2)
plt.plot(italya.Deaths, italya.Recovered, color="black", label= "Italyada olen-kurtulan sayilari")
plt.xlabel("Italya Olum Sayisi")
plt.ylabel("Italya Kurtulan Hasta Sayisi")

plt.show()