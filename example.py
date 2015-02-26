# -*- coding: utf-8 -*-
"""
Example to show the different options of the gaussian fit

Created on Thu Feb 26 10:04:44 2015

@author: kladtn
"""


import gauss_fit as gf
from skimage import io
import matplotlib.pyplot as plt
from numpy import *

# load example data
example_data = io.imread('./example_data2.tif',1)


# 
params = gf.fitgaussian(example_data, circular=False, centered=False)
print params
fitted_gaussian = gf.gaussian(*params)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(1, 1, 1)
plt.imshow(example_data, interpolation='none')
plt.contour(fitted_gaussian(*indices(example_data.shape)))

plt.show()

        
