# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:17:21 2020

@author: sumeyyeakay
"""

import pandas as pd



df=pd.read_csv("covid_19_data.csv")
print(df)


#Satir ve sutun sayilarini ogrenmek icin
print(df.shape)


#veri turu
print(df.dtypes)

#10 tane siralanmasi icin
print(df.head())

#son 10 deger
print(df.tail(10))


#string aalizi yapmak icin
print(df["Province/State"].describe())
"""
    [10 rows x 8 columns]
count                             9326
unique                             297
top       Diamond Princess cruise ship
freq                               129
Name: Province/State, dtype: object
"""

#sayisal olmayan butun sutunlarin analizleri
a = (df.describe(include=["O"]))

print(a)
    

ulkeler = (df["Country/Region"].value_counts())
print(ulkeler)


#turkiyenin corona virus sayilarini ogrenmek icin:
turkey = (df[df["Country/Region"] == "Turkey"])

print(turkey)












































