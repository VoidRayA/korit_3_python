class 클래스:

    def __init__(self, 변수1, 변수2):
        # 생성자 -> 인스턴스 변수 정의
        self.변수1 = 변수1
        self.변수2 = 변수2

    # toString() __str__이 __repr__ 보다 우선순위가 높음
    def __str__(self):
        return f"변수1: {self.변수1}, 변수2: {self.변수2}"

    # toString() 레퍼런스(개발단계, 디버깅)
    def __repr__(self):
        return f"변수11: {self.변수1}, 변수22: {self.변수2}"

    # 객체 비교
    def __eq__(self, other):
        return self.변수1 == other.변수1 and self.변수2 == other.변수2

    def __add__(self, other):
        return 클래스(self.변수1 + other.변수1, self.변수2 + other.변수2)

    def __sub__(self, other):
        return 클래스(self.변수1 - other.변수1, self.변수2 - other.변수2)

    def __contains__(self, item):
        return item in (self.변수1, self.변수2)

c1 = 클래스(10, 20)
print(c1)
c2 = 클래스(10, 20)
print(c1.__eq__(c2))
c3 = c1.__add__(c2)
print(c3)
print(c3.__contains__(10))