# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:26:52 2020

@author: sumeyyeakay
"""

import numpy as np
import pandas as pd

"""
#DATA SERIES

#seriler=pd.Series(data,index)
#data = sabit bi değer , liste numpy dizisi, dictionary

sayilar = [0,1,2,3,4,5,6,7,8,9]
numpy_array = np.array(sayilar)
print(numpy_array)
seriler = pd.Series(data=sayilar)
print(seriler)

#my index ile sayılar eşit olmalıdır yoksa kod hata verir

my_index = ['a','b','c','d','e','f','g','h','i','j']
seriler = pd.Series(data=sayilar, index=my_index,dtype=int)
print(seriler)

sözlük={'a':0 ,'b':1,'c':2,'d':3}
seriler= pd.Series(data=sözlük)
print(seriler)

print(seriler.ndim)
print(seriler.dtype)
print(seriler.shape)
"""

#Matematik işlemleri
sayılar=[0,1,2,3,4,5,6,7,8,9]
seriler=pd.Series(data=sayılar)

#Toplamını bulmak için
print(seriler.sum())

print(seriler.min())
print(seriler.max())

#Ortalamasını bulmak için
print(seriler.mean())     

#ortanca elemanı
print(seriler.median())

#varyansı hesaplama
print(seriler.var())

#standart sapma
print(seriler.std())

sayılar2 =[0,1,2,3,4,5,6,7,8,9]
seriler2 = pd.Series(data=sayılar2)
 
#serileri çarpıyor
print(seriler * seriler2)

































