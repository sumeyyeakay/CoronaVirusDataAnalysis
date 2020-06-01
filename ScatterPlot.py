# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:34:39 2020

@author: sumeyyeakay

    Tek grafik halinde gosterilmesi : Scatter Plot
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("covid_19_data.csv")

turkiye = df[df["Country/Region"] == "Turkey"]
italya = df[df["Country/Region"] == "Italy"]
ispanya = df[df["Country/Region"] == "Spain"]


#3ulkenin analizlerini tek tabloda ulasmak icin;

plt.scatter(turkiye.Deaths, turkiye.Recovered, color="red", label= "Turkiyede olen-kurtulan sayilari")
plt.scatter(italya.Deaths, italya.Recovered, color="blue", label= "Italya olen-kurtulan sayilari")
plt.scatter(ispanya.Deaths, ispanya.Recovered, color="black", label= "Ispanya olen-kurtulan sayilari")

plt.xlabel("Olum Sayisi")
plt.ylabel(" Kurtulan Hasta Sayisi")
plt.title("Dunyadaki Coronovirus Analizi")
plt.legend()
plt.show()