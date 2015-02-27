# -*- coding: utf-8 -*-
"""
Example to show the different options of the gaussian fit
centered vs. non-centered, elliptical vs. circular

Created on Thu Feb 26 10:04:44 2015

@author: Nikolay Kladt, Image & Data Analyst, CECAD Imaging Facility
"""


import gauss_fit as gf
from skimage import io
import matplotlib.pyplot as plt
from numpy import *

""" generate plot for first example, a single fit on a 2d image """

# load example data
example_data = io.imread('./example_data.tif',1)

# fit gaussian twice - one circular and one elliptic 
params_elliptic = gf.fitgaussian(example_data, circular=False, centered=False)
params_circular = gf.fitgaussian(example_data, circular=True, centered=False)
fitted_elliptic_gaussian = gf.gaussian(*params_elliptic)
fitted_circular_gaussian = gf.gaussian(*params_circular)

# plot both fits on top of the original data
fig = plt.figure(facecolor='w')
fig.add_subplot(1, 2, 1)
plt.imshow(example_data, interpolation='none')
plt.contour(fitted_elliptic_gaussian(*indices(example_data.shape)))
plt.title('Gaussian fit (elliptical)')
fig.add_subplot(1, 2, 2)
plt.imshow(example_data, interpolation='none')
plt.contour(fitted_circular_gaussian(*indices(example_data.shape)))
plt.title('Gaussian fit (circular)')
plt.show()


""" generate plot for second example, a single fit on a 2d image
    centered vs. non-centered """
    
# load example data
example_data = io.imread('./example_data2.tif',1)
        
# fit gaussian twice - one centered one not centered
params_centered = gf.fitgaussian(example_data, circular=False, centered=True)
params_anywhere = gf.fitgaussian(example_data, circular=False, centered=False)
fitted_centered_gaussian = gf.gaussian(*params_centered)
fitted_anywhere_gaussian = gf.gaussian(*params_anywhere)

# plot both fits on top of the original data
fig = plt.figure(facecolor='w')
fig.add_subplot(1, 2, 1)
plt.imshow(example_data, interpolation='none')
plt.contour(fitted_centered_gaussian(*indices(example_data.shape)))
plt.title('Gaussian fit (centered)')
fig.add_subplot(1, 2, 2)
plt.imshow(example_data, interpolation='none')
plt.contour(fitted_anywhere_gaussian(*indices(example_data.shape)))
plt.title('Gaussian fit (not centered)')
plt.show()