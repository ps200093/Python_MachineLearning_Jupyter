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