# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:07:24 2022

@author: nuh_e
"""

import heartpy as hp
import matplotlib.pyplot as plt

sample_rate = 100 
data = hp.get_data('heartbeat.csv') # calls csv file

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

#runs the analysis
wd, m = hp.process(data, sample_rate)

#Visualize the plot of custom size
plt.figure(figsize = (3,4))
hp.plotter(wd, m)

for measure in m.keys():
    print('%s: %f' %(measure , m[measure]))