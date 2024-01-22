# 함수는 값을 여려개 return 가능

def sum_minus(a, b):
    sum = a + b
    minus = a - b
    return sum, minus

sum = 0
minus = 0

a = 100
b = 200

sum, minus = sum_minus(a, b)

print("a + b = ", sum)
print("a - b = ", minus)
