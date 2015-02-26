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

def gaussian(height, center_x, center_y, width_x, width_y, circular=False):
    """ Returns a gaussian function with the given parameters"""
    if circular:
        return lambda x,y: height*exp(-(((center_x-x))**2+((center_y-y))**2)/(2*width_x))
    else:
        return lambda x,y: height*exp(-(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)
    
    
def moments(data, circular=False, centered=False):
    """ Returns (height, x, y, width_x, width_y, circular) 
    the gaussian parameters of a 2D distribution by calculating its moments """
    total = data.sum()
    X, Y = indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total
    col = data[:, int(y)]
    width_x = sqrt(abs((arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = sqrt(abs((arange(row.size)-y)**2*row).sum()/row.sum())
    height = data.max()    
    if circular:
        width_x = (width_x + width_y)/2
        width_y = (width_x + width_y)/2
    if centered:
        x = float(data.shape[0]/2)
        y = float(data.shape[1]/2)
    print x
    print y
    return height, x, y, width_x, width_y
    
    
def fitgaussian(data, circular=False, centered=False):
    """ Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution found by a fit"""
    params = moments(data, circular=circular, centered=centered)     
    errorfunction = lambda p: ravel(gaussian(*p, circular=circular)(*indices(data.shape)) - data)  
    p, success = optimize.leastsq(errorfunction, params)
    return p
    

def fwhm(width):
    """ Calculates the full width half maximum for a given width
    only makes sense for circular gaussians """
    fwhm = 2*sqrt(2*log(2)*width) # standard fcn, see web
    return fwhm    