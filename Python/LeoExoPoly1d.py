"""
First trial with data plotting
"""
import numpy as np
import matplotlib.pyplot as plt

p = np.poly1d([666,0,1,2])

x = np.arange(-20,60,1)

print "Voici les antecedants :", x

print "Voici le polynome", p

# calcul des ordonnees
y = p(x)

print "Voici les ordonnees correspondant a l'interval -20 a 59: ", y

plt.plot(x, y, color ='blue', linewidth=2.5, linestyle="--")
plt.legend("polynome 666 x^3 + x + 2")
plt.show()
