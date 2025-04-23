# 논리 연산
data1 = 10
data2 =2

r1 = data1 == data2
r2 = data1 != data2
print(r1, r2)

r3 = r1 and r2
r4 = r1 or r2
print(r3, r4)
print(not r3 and r4)

# 맴버 연산자 (in, not in)
print("a" in "apple")
print("b" in "apple")
print("a" in ["a", "b", "c"])
print("d" in ["a", "b", "c"])
print("c" in ("a", "b", "c"))
print("d" in {"a", "b", "c"})
print("name" in {"name" : "김준일", "age" : 32})
print("address" in {"name" : "김준일", "age" : 32})
print("김준일" in {"name" : "김준일", "age" : 32}.values())

# 식별 연산자 (is, is not)
print([1,2,3,4] is [1,2,3,4])   # 객체 주소 비교
print([1,2,3,4] == [1,2,3,4])   # 값 비교
print(10 == 10)
print(10 is 10)

if data1 == data2:
    print(f"data1: {data1}이 data2: {data2} 같다.")
else:
    print(f"data1: {data1}이 data2: {data2} 다르다.")

if data1 == 2:
    print("data1이 2입니다.")
elif data2 == 2:
    print("data2가 2입니다.")
else:
    print("둘다 아닙니다.")