# python의 class 정의

class Student:
    # python은 class 메서드와 스태틱 메서드를 구분함
    # 클래스 변수(JAVA satatic 변수)
    name = "김준일(클래스변수)"
    age = "32(클래스변수)"

    def __init__(self):
        # 인스턴스 변수
        self.name = "김준일"
        self.age = 32

    # self=this 개념
    def toString(self):
        return f"Student(name: {self.name}, age: {self.age}, clsName: {self.__class__.name})"

    # 클래스 변수 접근 O
    @classmethod
    def toString2(cls):
        return f"Student(name: {cls.name}, age: {cls.age})"

    # 클래스 변수 접근 X
    @staticmethod
    def toString3(name, age):
        return f"Student(name: {name}, age: {age})"

print(Student.name)
print(Student.age)

s1 = Student()
print(s1.name)
print(s1.age)
print(s1.toString())
print(Student.toString2())  # Static