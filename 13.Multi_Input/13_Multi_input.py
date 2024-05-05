#tensorflow 미분 함수 적용
import tensorflow as tf
import numpy as np

# some parts of data
x_data = [[73, 90, 75],
          [93, 88, 93],
          [89, 91, 90],
          [96, 98, 100],
          [73, 66, 70]]
y_data = [[152.],
          [185.],
          [180.],
          [196.],
          [142.]]

# read_csv file
# data = np.loadtxt('score_data_set.csv', delimiter = ',', dtype = np.float32)
# x_data = data[:, 0:-1]
# y_data = data[:,[-1]]

x_data = np.array(x_data, dtype = np.float32)
y_data = np.array(y_data, dtype = np.float32)

#tf.random.nomal => 정규분포를 가지는 랜덤 변수
W = tf.Variable(tf.random.normal([3, 1]))
b = tf.Variable(tf.random.normal([1]))

learning_rate = 1e-5

def gradientDescent():
  with tf.GradientTape() as tape:
    model = tf.matmul(x_data, W) + b
    cost = tf.reduce_mean(tf.square((model - y_data)))
    gradients = tape.gradient(cost,(W,b))

    tf.optimizers.SGD(learning_rate).apply_gradients(zip(gradients,(W,b)))

for step in range(10001):
  gradientDescent()
  model = tf.matmul(x_data, W) + b
  cost = tf.reduce_mean(tf.square(model - y_data))

  if step % 2000 == 0:
    print(step, "W = ", '\n',W.numpy(), "b = ",b.numpy(), "cost = ",cost.numpy())

# model verification
accuracy = tf.reduce_mean((model - y_data))
print("Accuracy : ", 1 - accuracy.numpy())

# model test
test_x_input1 = int(input("input 1 score : "))
test_x_input2 = int(input("input 2 score : "))
test_x_input3 = int(input("input 3 score : "))
test_x = np.array([[test_x_input1, test_x_input2, test_x_input3]], dtype = 'float32')

result = tf.matmul(test_x, W) + b
print("%.2f" %result.numpy())
