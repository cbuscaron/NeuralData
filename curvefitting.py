# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 23:00:20 2014

@author: Camilo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import optimize, polyfit

n = 50

jitter_amp= 4.0

x= np.linspace(0,10,n)

jitter= jitter_amp*(np.random.random(n)-.5)

y= x+jitter

plt.plot(x,y,'o')
plt.show()


m,b = polyfit(x,y,1)
print [m,b]

plt.plot(x,y,'o', hold=True)
t =np.array([0,10])

plt.plot(t,m*t+b)
plt.show()


def fit_func(t, m, b):
        return m*t+b
        
        
p,cov = optimize.curve_fit(fit_func, x, y)

print 'P'
print p[0]
print p[1]


plt.plot(x,y,'o',hold=True)
t = np.array([0,10])
plt.plot(t,p[0]*t*p[1])

plt.show()


mean = 0.0
var = 1.0
sigma = np.sqrt(var)
x = np.linspace(-4,4,80)

plt.plot(x,mlab.normpdf(x,mean,sigma))
plt.show()


n = 20
x = np.linspace(-4,4,n)
jitter_amp =.1
jitter = jitter_amp*(np.random.random(n)-.5)
y= mlab.normpdf(x,mean,sigma)+jitter
plt.plot(x,y,'o')
plt.show()

def normal_fit(t,mean,sigma):
        return mlab.normpdf(t,mean,sigma)
        
        
        
p, conv= optimize.curve_fit(normal_fit, x, y)

print p


plt.plot(x,y,'o',hold = True)
plt.plot(x,normal_fit(x,p[0],p[1]), '-')
plt.legend(['Original', 'fit'])
plt.show()


