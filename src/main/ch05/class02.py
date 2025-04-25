"""
생성자를 통한 주입
"""

class 무기:
    def __init__(self, 공격력):
        self.공격력 = 공격력

    def 공격(self):
        pass

class 총(무기):
    def __init__(self, 공격력, 총알):
        super().__init__(공격력)
        self.총알 = 총알

    def 공격(self):
        print(f"총을 쏜다.(데미지: {self.공격력})")
        self.총알소비()
        
    def 총알소비(self):
        self.총알 -= 1
        print(f"현재 남은 총알: {self.총알}발")

class 칼(무기):
    def __init__(self, 공격력):
        super().__init__(공격력)

    def 공격(self):
        print(f"칼을 휘두른다.(데미지: {self.공격력})")

class 손:
    def __init__(self, 타입, 무기):
        self.타입 = 타입 #손의 좌우를 확인하는 타입
        self.무기 = 무기

    def 손으로_공격(self):
        print(f"{self.타입}으로 공격합니다.")
        self.무기.공격()

오른손 = 손("오른손", 칼(50))
# 총1 = 총(100, 7)
왼손 = 손("왼손", 총(100, 7))
print(왼손.무기.총알)

오른손.손으로_공격()
while 왼손.무기.총알 > 0:
    왼손.손으로_공격()