# import lib
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (8, 5)

# slope 1 graph
x_data = np.array([1.0, 2.0, 3.0], dtype = np.float32)
y_data = np.array([1.0, 2.0, 3.0], dtype = np.float32)
W = tf.Variable(tf.random.normal([1]))

W_val = []
cost_val = []

for i in range(-30, 50):   # 분포 정의
  W_curr = i * 0.1
  cost_curr = tf.reduce_mean(tf.square(W_curr * x_data - y_data)) # MSE 평균제곱오차

  W_val.append(W_curr)
  cost_val.append(cost_curr)

# plot and show
plt.plot(W_val, cost_val)
plt.xlabel("W_val")
plt.ylabel("cost_val")
plt.show()