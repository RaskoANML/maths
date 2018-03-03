"""
I am plotting my first polynome
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,1)

p = np.poly1d([666,0,1,2])

print p

y = p(x)

plt.plot(x, y)
plt.show()
 
