# 파이썬 기본 문법

# 문장 출력
print('Hello, World!')      # Hello, World!
print("'Hello, World!'")    # 'Hello, World!'
print("\"Hello, World!\"")  # "Hello, World!"
print("\\Hello, World!\\")  # \Hello, World!\
print('Hello, \nWorld!')    # Hello,
                            # World!

# 변수 (variable)
score = 100
print(score)    # 100
score = score - 10
print(score)    # 90
score = 30
print(score)    # 30

# 문자열 포맷팅
x = 3.14
y = 6.02
print("x : %f y : %f" %(x, y))  # x : 3.140000 y : 6.020000
print("x + y = %d" %(x + y))    # x + y = 9
print("x + y = %f" %(x + y))    # x + y = 9.160000
print("x + y = %0.2f" %(x + y)) # x + y = 9.16

a = "안녕"
b = "하세요."
print(a + b)    # 안녕하세요.

# import Tensorflow lib
import tensorflow as tf

# output sentence
hello = tf.constant("Hello, World!")

print(type(hello))                      # <class 'tensorflow.python.framework.ops.EagerTensor'>
print(hello)                            # tf.Tensor(b'Hello, World!', shape=(), dtype=string)
print(hello.numpy())                    # b'Hello, World!'
print(hello.numpy().decode('utf-8'))    # Hello, World!