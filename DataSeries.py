# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:27:59 2020

@author: sumeyyeakay
"""

import pandas as pd

sayılar = [0,1,2,3,4,5,6,7,8,9]
seriler = pd.Series(data=sayılar)

print(seriler[seriler>5])

print(seriler[seriler>seriler.mean()])

print(seriler[seriler==4])

print(seriler[seriler <5])
