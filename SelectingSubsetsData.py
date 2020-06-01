# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:54:23 2020

@author: sumeyyeakay
"""

import pandas as pd

#corona virusun goruldugu heryeri gormek icin
df = pd.read_csv("covid_19_data.csv")
print(df)

#sehirleri gormek icin
first = df["Province/State"]
print(first)

#hem ulke hem de sehire ulasmak icin
second = df[["Province/State", "Country/Region", "Deaths"]]
print(second)

#bazi satir ve sutunlara ulasmak icin:
#loc(satir,sutun)
c1 = df.loc[1]
print(c1)

#butun sutunlari alamk icin
c3 = df.loc[:, "Province/State"]

#index degerinin hepsine ulasmak icin
c6 = df.iloc[30042]
print(c6)


#belli bir sarti saglayanlarin gorulmesi icin
Deaths = df[df.Deaths>1000]
print(Deaths)

