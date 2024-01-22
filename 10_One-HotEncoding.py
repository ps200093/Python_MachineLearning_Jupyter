#import library
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

x_data = [[1,2,1,1],[2,1,3,2],[3,1,3,4],
          [4,1,5,5],[1,7,5,5],[1,2,5,6],
          [1,6,6,6],[1,7,7,7]]

y = [2, 2, 2, 1, 1, 1, 0, 0]
y_data = tf.one_hot(y, 3)   # depth : 3
y_data = tf.reshape(y_data, [-1, 3])

x_data = np.array(x_data, dtype = np.float32)
y_data = np.array(y_data, dtype = np.float32)

# convert data to OneHot vector
#y_data = [[0,0,1],[0,0,1],[0,0,1],
#          [0,1,0],[0,1,0],[0,1,0],
#          [1,0,0],[1,0,0]]

# initialize variables
W = tf.Variable(tf.random.normal([4, 3]))   # feature : 4, class : 3
b = tf.Variable(tf.random.normal([3]))

learning_rate = 1e-1

# Model define
def softmax_classfier():
  with tf.GradientTape() as tape:

    #cost/loss function
    model_LC = tf.matmul(x_data, W) + b
    cost = tf.reduce_sum(tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = model_LC, labels = y_data)))

    gradients = tape.gradient(cost,(W,b))
    tf.optimizers.SGD(learning_rate).apply_gradients(zip(gradients,(W,b)))


for step in range(2001):    # 2000 iteration
  softmax_classfier()
  model_LC = tf.matmul(x_data, W) + b
  model = tf.argmax(tf.nn.softmax(model_LC),1)
  cost_fn = tf.reduce_sum(tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = model_LC, labels = y_data)))

  accuracy = tf.reduce_mean(tf.cast(tf.equal(model, tf.argmax(y_data,1)),tf.float32))

  if step % 100 == 0:   # show every 100 times
    print("\n--------------------------------------\n", "step : ", step, '\nAccuracy = ', accuracy.numpy(), '\ncost = ', cost_fn.numpy())