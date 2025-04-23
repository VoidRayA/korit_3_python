studentDict = dict()
studentDict = {
    "name": "심민호",
    "age": 25
}

# dict 값 추가
studentDict["address"] = "부산"
print(studentDict["address"])

# dict와 list의 값 추가 차이
anyList = []
anyList.append("test")
print(anyList)

# dict 값 조회
name = studentDict.get("name")
print(name)
print(studentDict["age"])

# dict 값 수정
studentDict["address"] = "서울"
print(studentDict["address"])

# dict 값 삭제
del studentDict["age"]
print(studentDict)
studentDict.pop("name")
print(studentDict)

# dict Key, Value 한쌍 => 아이템
studentDict["name"] = "김미진"
print(studentDict.items())
print(list(studentDict.items())[0])
key, value = list(studentDict.items())[0]
print(f"key: {key}, value: {value}")

# dict Key만 모두 뽑아 보고 싶을 때
print(studentDict.keys())
print(list(studentDict.keys()))

# dict 값들만 모두 뽑아 보고 싶을 때
print(studentDict.values())
print(list(studentDict.values()))

searchKey = "code"

students = [
    {
        "code": 1,
        "name": "심민호"
    },{
        "code": 2,
        "name": "윤현지"
    },{
        "code": 3,
        "name": "이동규"
    }
]

result = []

i = 0

while i < len(students):
    student = students[i]
    result.append(student[searchKey])
    i += 1

print(result)

result = {}

i = 0

while i < len(students):
    student = students[i]
    keys = list(student.keys())
    j = 0
    while j < len(keys): # student[key] - code, name을 차례대로 추가
        key = keys[j]
        j += 1
        if key in result: # student[key] - code 추가
            result[key].append(student[key])
            continue # break와 같음
        result[key] = [student[key]]
    i += 1

print(result)