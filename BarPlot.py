# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:47:05 2020

@author: sumeyyeakay

    Net bilgiler oldugunda kullanilmasi daha kullanisli olur
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("covid_19_data.csv")

turkiye = df[df["Country/Region"] == "Turkey"]
italya = df[df["Country/Region"] == "Italy"]
ispanya = df[df["Country/Region"] == "Spain"]
"""
plt.bar(turkiye.Deaths, turkiye.Recovered)
plt.show()


sayi = np.array([1,2,3,4,5,6,7,8,9])
karesi = sayi **2

plt.bar(sayi,karesi)
plt.xlabel("Sayi degeri")
plt.ylabel("Sayinin karesi")

plt.show()

"""
#100 bin kisiye dusen yogun yatak sayisi
ulke = ["Turkiye", "ABD" , "Almanya", "Ispanya", "Fransa", "Guney Kore" , "Japonya"]
oran = [40,34.7,29.2,12.5,11.6,10.6,9.7]
plt.xlabel("Ulkeler")
plt.ylabel("Oranlar")
plt.title("Yogun bakim yatak sayisi")
plt.bar(ulke,oran)
plt.show()