# sigmoid 예시
# Example of Sigmoid

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 임의의 데이터 생성
# Generate data
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

# Set Learning_rate
learning_rate = 0.01

# 1) Define Model
def logisticRegression():
    with tf.GradientTape() as tape:
        hyp = tf.sigmoid(tf.matmul(x_data, W) + b)  # H(x) = Wx + b

        # tf.reduce_mean => reduction mean
        cost = -tf.reduce_mean(y_data * tf.math.log(hyp) + (1 - y_data) * tf.math.log(1 - hyp))  # Cross-Entropy Loss
        gradients = tape.gradient(cost, (W, b))  # Calculate gradients using automatic differentiator

        tf.optimizers.SGD(learning_rate, momentum=0.0).apply_gradients(
            zip(gradients, (W, b)))  # Update 'W' and 'b' using SGD with learning_rate


cost_val = []  # For save the cost value

# 2) Model training
for step in range(10001):  # == max_iter == epoch
    logisticRegression()
    hyp = tf.sigmoid(tf.matmul(x_data, W) + b)
    cost = tf.reduce_mean(tf.square(hyp - y_data))
    cost_val.append(cost)
    if step % 2000 == 0:
        prediction = tf.cast(hyp > 0.5, dtype=tf.float32)   # Convert hyp into binary predictions
        accuaracy = tf.reduce_mean(tf.cast(tf.equal(prediction, y_data), dtype=np.float32))

        print("\nStep : ", step,
              "\nHyp = ", '\n', hyp.numpy(),  # Hypothesis
              '\n', "b = ", b.numpy(),
              '\n', "cost = ", cost.numpy(),
              '\n', "accuaracy = ", accuaracy.numpy())  # Model accuracy

print("Model train output : ", prediction.numpy())

# 3) Model test
print("\nModel test")
test_X1 = int(input("input number1 : "))
test_X2 = int(input("input number2 : "))
x_test = np.array([[test_X1, test_X2]], dtype = np.float32)
output = tf.sigmoid(tf.matmul(x_test, W) + b).numpy()
test_pred = tf.cast(output > 0.5, dtype=tf.float32)
print("Test pred : ",test_pred.numpy()[0][0])


# 4) Plot Cost Function graph
plt.plot(cost_val)
plt.title('Cost Function')
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.show()

# 5) Plot with seaborn
import pandas as pd
import seaborn as sns

# Convert to numpy arrays
y_data = np.array(y_data)
hyp = np.array(hyp)

# Create a DataFrame with y_data and hyp
data = {"y_data": y_data.flatten(), "hyp": hyp.flatten()}
df = pd.DataFrame(data)

# Create a scatterplot
sns.scatterplot(data=df, x="hyp", y="y_data", hue="y_data", marker="o", s=100)

# Show the plot
plt.show()

# ---------------------------------------------------------------------------

# 6) DecisionBoundary
scatter = plt.scatter(x_data[:, 0], x_data[:, 1],
                      c=y_data.flatten(),
                      cmap='viridis',
                      label='feature1,feature2')

# Create a range of values for the hypothesis
hyp_range = np.linspace(0, 7, 100)

# Calculate the decision boundary using the model weights (W) and bias (b)
y_boundary = -(W[0] * hyp_range + b.numpy()) / W[1]

# Plot the decision boundary with a red line
plt.plot(hyp_range, y_boundary,
         color='red',
         linestyle='-',
         label='model')

plt.ylim(-1, 5)
plt.legend(handles=scatter.legend_elements()[0],
           labels=['feature1', 'feature2'])

# Show the plot
plt.show()
