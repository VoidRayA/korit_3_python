from Tools.scripts.texi2html import kwprog


def fx1():
    return "함수1", "함수2", "함수3"

# tuple로 이루어져 있음
r1, r2, r3 = fx1()
print(r1, r2, r3)

r4, r5, r6 = "함수4", "함수5", "함수6"
print(r4, r5, r6)

r7 = "함수7", "함수8"
print(r7)

# 기본값 매개변수
def fx2(name, membershipType="일반회원"):
    return {
        "회원종류": membershipType,
        "이름" : name
    }

member1 = fx2("김준일")
print(member1)
member2 = fx2("김준이", "골드회원")
print(member2)
member3 = fx2("김준삼", "일반회원")
print(member3)

# 키워드 매개변수(인자) -> 내가 어떤 매개변수에 값을 전달할지 명시
def fx3(name, membershipType, address, phone, registerDate):
    return {
        "회원종류": membershipType,
        "이름": name
    }

# member4 = fx3("김준사", "VIP")
member5 = fx3(
    phone="전화번호",
    name="김준사",
    address="주소",
    membershipType="VIP",
    registerDate="가입일자")

# 가변인자 *변수명(args), **변수명(kwargs)
def fx4(*aa):
    print(aa)

fx4(1,2,3,4,5,6,7)

def fx5(*aa, bb):
    print(f"aa: {aa}")
    print(f"bb: {bb}")

fx5(1,2,3,4,5,6,7, bb=8)

def fx6(address, **cc):
    print(f"cc: {cc}")
    print(f"address: {address}")

fx6(address="부산", name="김준일", age=32)

"""
매개변수 순서 요약
1. 일반 인자
2. 기본값이 있는 인자
3. *args(가변인자-Tuple(앞에 위치))
4. 키워드 전용 인자
5. **kwargs(뒤에 위치)
"""

def fx(a, b=0, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

fx(10, b=20, args=(10, 20, 30, 40), name="김준일", age=32)
fx(10, 20, 30, 40, 50, name="김준일", age=32)
