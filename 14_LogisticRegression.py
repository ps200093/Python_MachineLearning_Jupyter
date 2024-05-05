# sigmoid 예시
# Example of Sigmoid
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# 임의의 데이터 생성
# Generate random data
x_data = np.array([[1, 2],
                   [2, 3],
                   [3, 1],
                   [4, 3],
                   [5, 3],
                   [6, 2]], dtype=np.float32)

y_data = np.array([[0],
                   [0],
                   [0],
                   [1],
                   [1],
                   [1]], dtype=np.float32)

# tf.random.nomal => 정규분포를 가지는 랜덤 변수
# random_state와 동일한 기능

# tf.random.normal => Random variable with a normal distribution
# Equivalent to random_state
W = tf.Variable(tf.random.normal([2, 1]))
b = tf.Variable(tf.random.normal([1]))

learning_rate = 0.01


# 작게 크게 바꿔서 해보기

def logisticRegression():
    with tf.GradientTape() as tape:
        hyp = tf.sigmoid(tf.matmul(x_data, W) + b)

        # tf.reduce_mean => 평균
        cost = -tf.reduce_mean(y_data * tf.math.log(hyp) + (1 - y_data) * tf.math.log(1 - hyp))  # Cross-Entropy Loss
        gradients = tape.gradient(cost, (W, b))

        # 자동미분기
        tf.optimizers.SGD(learning_rate).apply_gradients(zip(gradients, (W, b)))


for step in range(10001):  # = max_iter = epoch
    logisticRegression()

    if step % 2000 == 0:
        hyp = tf.sigmoid(tf.matmul(x_data, W) + b)
        cost = tf.reduce_mean(tf.square(hyp - y_data))

        prediction = tf.cast(hyp > 0.5, dtype=tf.float32)

        accuaracy = tf.reduce_mean(tf.cast(tf.equal(prediction, y_data), dtype=np.float32))

        print(step, '\n',
              "Hyp = ", '\n', hyp.numpy(),  # 예상 출력값
              '\n', "b = ", b.numpy(),
              '\n', "cost = ", cost.numpy(),
              '\n', "accuaracy = ", accuaracy.numpy())  # 모델 정확도
