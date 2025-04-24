# 람다 함수
"""
JAVA
@FunctionInterface
public interface Addition {
    void add(int a);
}

public class Test {
    public static int aaa() {
        return 10 + n;
    }

    public static void main (String[] args){
        int number = 20;
        Addition a = n -> {
            System.out.println(n);
            return n + number;
        }
        int result = a.add(10);
        System.out.println(result);
    }
}
"""

# Python 람다 함수
# lambda 매개변수: 표현식
def add(num1, num2):
    return num1 + num2
print(add(10,20))
add = lambda num1, num2: num1 + num2
print(add(10,20))

students = [("김준일", 90), ("김준이", 85), ("김준삼", 95)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

numbers = (1,5,23,2,6,4)
print(numbers)
numbers2 = list(map(lambda num: num * 2, numbers))
print(numbers2)

print(numbers)
numbers3 = list(filter(lambda num: num % 2 == 0, numbers ))
print(numbers3)

numbers4 = list(map(lambda num: f"<h1>{num}</h1>", numbers3))
print(numbers4)

