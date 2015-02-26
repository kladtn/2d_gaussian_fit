# -*- coding: utf-8 -*-
"""
Simple code to perform a 2D gaussian fit. The original code was found on the
Scipy Cookbook and was modified to support more fit-parameters:
1.  fitting starting centered on the 2D data or on the position of the 
    maximum value of the 2D data
2. fitting a circular gaussian (width is the same in x and y)
Also, the full width half maximum (useful for circular fits) can be obtained.

Created on Wed Aug 20 16:20:07 2014
@author: Original Code found on the Scipy Cookbook, modified by Nikolay Kladt
"""

from scipy import optimize
from numpy import *

def gaussian(height, center_x, center_y, sigma_x, sigma_y, circular=False):
    """ Returns a gaussian function with the given parameters"""
    if circular:
        return lambda x,y: height*exp(-(((center_x-x)/sigma_x)**2+((center_y-y)/sigma_x)**2)/2)
    else:
        return lambda x,y: height*exp(-(((center_x-x)/sigma_x)**2+((center_y-y)/sigma_y)**2)/2)
    
    
def moments(data, circular=False, centered=False):
    """ Returns (height, x, y, width_x, width_y, circular) 
    the gaussian parameters of a 2D distribution by calculating its moments """
    total = data.sum()
    X, Y = indices(data.shape)
    if centered:
        x = float(data.shape[0]/2)
        y = float(data.shape[1]/2)
    else:
        x = (X*data).sum()/total
        y = (Y*data).sum()/total
    col = data[:, int(y)]
    sigma_x = sqrt(abs((arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    sigma_y = sqrt(abs((arange(row.size)-y)**2*row).sum()/row.sum())
    height = data.max()    
    if circular:
        sigma_x = (sigma_x + sigma_y)/2
        sigma_y = (sigma_x + sigma_y)/2
    
    return height, x, y, sigma_x, sigma_y
    
    
def fitgaussian(data, circular=False, centered=False):
    """ Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution found by a fit"""
    params = moments(data, circular=circular, centered=centered)     
    errorfunction = lambda p: ravel(gaussian(*p, circular=circular)(*indices(data.shape)) - data)  
    p, success = optimize.leastsq(errorfunction, params)
    if circular: # make sure that we have something sensible to sigma_y
        p[4] = p[3]
    return p
    

def fwhm(sigma):
    """ Calculates the full width half maximum for a given width
    only makes sense for circular gaussians """
    fwhm = 2 * sqrt(2 * log(2)) * sigma # standard fcn, see web
    return fwhm    