# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 21:29:35 2014

@author: Camilo
Creating Data Frams
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.random.randint(0,100,10)
b = np.random.random(10)
c = ['male', 'female']*5

df = pd.DataFrame({'ints':a, 'floats':b, 'gender':c})
df.describe()
print df.max()

df.groupby('gender').mean