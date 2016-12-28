
"""
Code example for the use of matplotlib
"""

import matplotlib.pyplot as plt

radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
area = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
plt.plot(radius, area)
#plt.show()
plt.savefig('examples/plot.png', bbox_inches='tight')
