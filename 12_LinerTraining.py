import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# data set
x_data = [1, 2, 3, 4]
y_data = [2, 1, 4, 3]

#tf.random.nomal => 정규분포를 가지는 랜덤 변수
W = tf.Variable(tf.random.normal([1]))
b = tf.Variable(tf.random.normal([1]))

# learning rate = 0.01
learning_rate = 0.01

def gradientDescent():  # Create Model
  model = W * x_data + b  # y = H(x) + b
  W_gradient = tf.reduce_mean((model - y_data) * x_data)
  b_gradient = tf.reduce_mean((model  - y_data))

  W_descent = W - learning_rate * W_gradient
  b_descent = b - learning_rate * b_gradient

  # update weights
  W.assign(W_descent)
  b.assign(b_descent)

for step in range(10001): # 10000 iteration
  gradientDescent()
  model = W * x_data + b
  cost = tf.reduce_mean(tf.square(model - y_data))

  if step % 1000 == 0:  # show every 1000 times
    print("\n--------------------------------------\n", "step : ", step,
          '\nW = ', W.numpy(), '  b = ', b.numpy(),
          '\ncost = ', cost.numpy())

# real data & Liner model
plt.scatter(x_data, y_data)
plt.plot(x_data, model, color = 'green')
plt.show()
