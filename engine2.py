import matplotlib.pyplot as plt
import numpy as np

bingus_x = np.array([[0.0],
                     [1.0],
                     [1.0],
                     [0.0]])

bingus_y = np.array([[1.0],
                     [1.0],
                     [2.0],
                     [2.0]])

plt.plot(bingus_x, bingus_y)
# plt.plot(xcoords_b, ycoords_b)
plt.xlabel("x")
plt.ylabel("y")
plt.show()