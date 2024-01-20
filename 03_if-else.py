# if/else 조건문
score = int(input("점수 입력 : "))

# 0 ~ 100의 정수 입력
if score > 100 or score < 0:
    print("잘못된", end=' ')
else:
    if score >= 90:
        print("A", end='')
    else:
        if score >= 80:
            print("B", end='')
        else:
            if score >= 70:
                print("C", end='')
            else:
                if score >= 60:
                    print("D", end='')
                else:
                    print("F", end='')
print(" 학점입니다.")