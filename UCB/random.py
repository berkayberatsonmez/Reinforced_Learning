# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 08:22:09 2022

@author: berkayberatsonmez
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

import random

N = 10000
d = 10
toplam = 0
secilenler = []
for n in range(0,N):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = veriler.values[n,ad] #n. satır = 1 ise o zaman odul 1
    toplam = toplam + odul
    
plt.hist(secilenler)
plt.show()





