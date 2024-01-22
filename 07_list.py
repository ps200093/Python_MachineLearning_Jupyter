# 리스트에 값 추가
numList = [0]

numList.append(2)
numList.append(4)
numList.append(6)
numList.append(8)

print(numList)
print("\n")
# 반복문을 사용한 방법
numList = []

for i in range(1,5):
  numList.append(2*i)
print(numList)
print("\n")

# 리스트 슬라이싱
numList = [10, 20, 30, 40]

print(numList[0:3])
print("\n")

print(numList[2:4])
print("\n")

print(numList[:3])
print("\n")


print(numList[1:])
print("\n")