# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:44:03 2020

@author: sumeyyeakay

    Histogram grafikleri
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("covid_19_data.csv")

turkiye = df[df["Country/Region"] == "Turkey"]
italya = df[df["Country/Region"] == "Italy"]
ispanya = df[df["Country/Region"] == "Spain"]

plt.hist(italya.Deaths,bins=10)

plt.xlabel("Olum Sayisi")
plt.ylabel(" Kurtulan Hasta Sayisi")
plt.title("Italya Coronovirus Analizi")

plt.show()