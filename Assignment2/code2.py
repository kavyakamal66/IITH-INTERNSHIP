# -*- coding: utf-8 -*-
"""code2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17nDT9wvyqNjcGQk2MfaceKk48Bp7Pwbb
"""

import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np

#assume value of slope
m=2

# defining the function
def function(x):
    
    return m*x
  
# calculating its derivative
def deriv(x):
    return derivative(function, x)
  
# defininf x-axis intervals
y = np.linspace(-6, 6)
  
# plotting the function
plt.plot(y, function(y), color='purple', label='y=mx')
  
# plotting its derivative
plt.plot(y, deriv(y), color='green', label='(dy/dx)=m')
  
# formatting
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='upper left')
plt.grid(True)