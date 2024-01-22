# sin 그래프 plot

# import lib
import matplotlib.pyplot as plt
import numpy as np

# graph size
plt.rcParams['figure.figsize'] = (12, 6)

# x range
x = [0.01 * i for i in range(-200, 200)]

# y range
y = [np.sin(j * np.pi) for j in x]

# plot and show
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Sin(x)')
plt.show()
