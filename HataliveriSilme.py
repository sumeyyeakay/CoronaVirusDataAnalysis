# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:19:21 2020

@author: sumeyyeakay

hatali verileri bulmak ve silmek & Group By
"""

import pandas as pd

df= pd.read_csv("covid_19_data.csv")

#silama yapmak icin
#en fazla olumun oldugu yerleri gormek icin
al = df.sort_values(by = 'Deaths', ascending=False).head(20)

#indeci silmek icin
delete = df.drop(12969)
print(df.sort_values(by = 'Deaths', ascending=False).head(20))
#2.yol olarak
df.drop(12649, inplace=True)
print(df.sort_values(by = 'Deaths', ascending=False).head(20))


#SNo sutununu silmek icin
df = df.drop("SNo" , axis= 1)
print(df.sort_values(by = 'Deaths', ascending=False).head(20))
# 2.yol olarak
#df= df.drop(columns="SNo")
print(df.columns)

#Gruplama islemi : Group By
print(df.groupby("Province/State")["Deaths"].mean().head(10))
print(df.groupby("Province/State")["Deaths"].max().head(10))

print(df.gr)