from setuptools.build_meta import prepare_metadata_for_build_wheel

a = int(input("a입력: "))
b = int(input("b입력: "))

print(a, b)
print(type(a))
print(type(b))

# "10 20"
number = input("두 수 입력: ").split()
print(number)

number1, number2 = map(lambda n: int(n), input("두 수 입력: ").split())
print(number1)
print(number2)

def parseInt(n):
    return int(n)
number3, number4 = map(parseInt, input("두 수 입력: ").split())
print(number3)
print(number4)

number5, number6 = list(map(int, input("두 수 입력: ").split()))
print(type(number5))
print(number6)

parseInt = lambda n: int(n)
map(parseInt, ["10", "20"])

number7, number8 = list(map(int, input("두 수 입력: ").split()))
print(number7)
print(number8)