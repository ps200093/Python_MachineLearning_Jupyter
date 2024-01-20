# for 문

for i in range(5):
    print(i, end=' ')  # 0 1 2 3 4
print('\n')

for i in range(0, 5, 2):
    print(i, end=' ')  # 0 2 4
print('\n')

for i in range(3, 5):
    print(i, end=' ')  # 3 4
print('\n')

numList = [5, 10, 6, 2, 7]
for i in numList:  # 리스트의 각 요소 접근
    print(i, end=' ')  # 5 10 6 2 7
print('\n')

# while 문

i = 0
while i < 5:
    print(i, end=' ')  # 0 1 2 3 4
    i += 1
print('\n')

i = 3
while i < 5:
    print(i, end=' ')  # 3 4
    i += 1
print('\n')

i = 3
while i < 5:
    print(i, end=' ')  # 3
    i += 2
print('\n')

i = 0
while i < len(numList):
    print(numList[i], end=' ') # 5 10 6 2 7
    i += 1