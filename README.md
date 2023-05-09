# rv_curve_jurapackage

## JURA IV python example, May 09, 2023

This package allows you to create a radial velocity plot of a star orbited by a planet.

### Usage Instructions

#import libraries
import numpy as np
import matplotlib.pyplot as plt
#import our rv curve.class
from rv_curve_jurapackage.rv_curve_module import rv_curve_class

#Create the instance
rv = rv_curve_class(t0=0., p=10., e=0.5, w=np.pi/3, k=10., t_init=0., t_end=25.)
#Use the plot method to create the plot
rv.plot() 
