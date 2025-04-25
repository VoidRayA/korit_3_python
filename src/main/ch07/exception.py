if __name__ == '__main__':
    print("예외처리")

    numbers = [1,2,3,4,5]

    try:
        print(numbers[5])
    except IndexError as e:
        print(e)
        print("범위 초과입니다.")

    try:
        print(numbers[5])
    except Exception as e:
        print(e)
        print("범위 초과입니다.")

    try:
        print("예외 강제 발생")
        raise TypeError("자료형을 맞춰써주세요.")
    except TypeError as e:
        print(e)