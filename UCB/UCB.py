# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 08:37:18 2022

@author: berkayberatsonmez
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

N = 10000 #10.000 tıklama
d = 10 #toplam 10 ilan var
oduller = [0] * d #ilk başta bütün ilanların odulu 0 / Ri(n)
tiklamalar = [0] * d #Ni(n)
toplam = 0 #toplam ödül
secilenler = []
for n in range(1,N):
    ad = 0 #seçilen ilan
    max_ucb = 0
    for i in range(0,d): #max'tan büyük bir ucb çıktı
        if (tiklamalar[i] > 0) :
            ortalama = oduller[i] / tiklamalar[i]
            delta = math.sqrt(3/2 * math.log(n)/tiklamalar[i])
            ucb = ortalama + delta
        else:
            ucb = N*10
        if max_ucb < ucb:
            max_ucb = ucb
            ad = i
        
    secilenler.append(ad)   
    tiklamalar[ad] = tiklamalar[ad] + 1
    odul = veriler.values[n,ad]
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul

print('Toplam Odul:')
print(toplam)

plt.hist(secilenler)
plt.show()


