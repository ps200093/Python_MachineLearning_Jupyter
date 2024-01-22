import numpy as np
import matplotlib.pyplot as plt

# 입력을 0-1 사이의 값으로 변환
# 비선형 함수로 주로 이진 분류 모델의 활성화 함수로 사용


# 시그모이드 함수 정의
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 입력값 생성 (-7부터 7까지)
x = np.linspace(-7, 7, 200)

# 시그모이드 함수 적용
sigmoid_values = sigmoid(x)

# 시각화
plt.plot(x, sigmoid_values, label='Sigmoid')
plt.xlabel('x values')
plt.ylabel('Sigmoid(x)')
plt.title('Sigmoid Function')
plt.legend()
plt.grid(True)
plt.show()
