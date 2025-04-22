# list 동작

numbers = [1, 2, 3, 4, 5]

print(numbers[0])
print(numbers[0:3])
print(numbers[3:])
print(numbers[:3])
print(numbers[-3:])
print(numbers[:-3])
print("부산 동래구"[3:])
print((1,2,3,4)[2:])
print((1,2,3,4)[:2])
print((1,2,3,4)[2])
print((1,2,3,4))

anyList = [[1, "유지현", [3,4,[7,"김준이"],6]]]

print(anyList[0][2][2][1])  # 김준이만 출력
print(anyList[0][2][1:3])   # 3번째 리스트에서 4에서 6까지

# 연산자
"""
+, -, *, **(제곱), /, //(몫), %
"""

print(3//2)
print(3**2)
print("*", "\n", "*" * 2, "\n", "*" * 3, sep="" )
i = 0
while i < 5:
    print("*" * (i + 1))
    i += 1  # i++(java)

i = 0
while i < 5:
    print("*" * (5 - i))
    i += 1

print([1,2,3] + [4,5,6])
print([1,2,3] * 3)

print(len([1,2,3]))

anyList = [1,2,3,4]

i = 0
while i < len(anyList):
    print(anyList[i])
    i += 1

print(str(3) + "hi")
print(int("1") + 2)
print(bool(True))

# del 키워드로 삭제할 때 값이 꼭 존재해야한다.
del anyList[2]
print(anyList)

try:
    anyList.pop(4)
    print(anyList)
except Exception as e:
    print("해당 리스트의 범위를 초과한 참조입니다.")

anyList = [1,5,2,3,9]
# copyAnyList = anyList.copy()
copyAnyList = anyList[:]
copyAnyList.sort()
copyAnyList.reverse()
print(anyList)
print(copyAnyList)

print([1,2,3,4,5] == [1,3,2,4,5])
anyList = [1,2,3,4,5]
anyList2 = [1,3,2,4,5]
print(id(anyList) == id(anyList2))
print(id(anyList), id(anyList2))

anyList = [1,2,3]
anyList2 = [4,5]
print(id(anyList))
anyList = anyList + anyList2
print(id(anyList))
anyList.extend([6,7])
print(id(anyList))
