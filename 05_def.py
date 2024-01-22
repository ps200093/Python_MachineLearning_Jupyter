# 함수를 정의하지 않고 코드 작성

num1 = int(input("정수1 ==> "))
num2 = int(input("정수2 ==> "))
sum = num1 + num2
print("결과 : ", sum)

num1 = int(input("정수1 ==> "))
num2 = int(input("정수2 ==> "))
sum = num1 + num2
print("결과 : ", sum)

# def를 이용한 나만의 함수 정의
def sumab():  # 두 번의 정수 입력 후, 덧셈
    num1 = int(input("정수1 입력 : "))
    num2 = int(input("정수2 입력 : "))

    return num1 + num2

print("sumab 실행")
sum = sumab()
print("결과 : ", sum)

print("sumab 실행")
print("결과 : ", sumab())

# 함수를 정의하여 사용하면 코드의 중복을 제거할 수 있다.


# 같은 기능을 하는 코드는 무수히 많다.
def sum(a, b):
    result = 0
    result = a + b
    return result

num1 = int(input("정수1 ==> "))
num2 = int(input("정수2 ==> "))
print("결과 : ", sumab(num1, num2))