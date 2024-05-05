import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# variable range
array = np.linspace(-5, 5, 100)

plt.axvline(x=0, color='r', linestyle='--', linewidth=1)
plt.axhline(y=0, color='0', linestyle='-', linewidth=1)
plt.axhline(y=1, color='0', linestyle='-', linewidth=1)
plt.plot(array, sigmoid(array))
plt.show()
