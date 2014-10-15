# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import matplotlib.pyplot as p


data = np.random.rand(1000)

p.plot(data)

p.show()

datan = np.random.rand(1000)

p.hist(datan)

p.show()

datan = np.random.randn(1000)

p.hist(datan)

p.show()

datan = np.random.randn(1000)

p.hist(datan, 20, normed= True, cumulative=True)
p.xlabel('Random Normalized Data')

p.show()

spikecounts = np.random.rand(8)*20

x = np.arange(0, 360, 45)

print x

p.bar(x, spikecounts, width =45)
p.axis([0, 360,0, 16])
p.show()

p.polar(x*np.pi/180, spikecounts)

spikecounts2 = np.append(spikecounts,spikecounts[0])

theta= np.arange(0,361,45)*np.pi/180

p.polar(theta,spikecounts2)