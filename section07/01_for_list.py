# for문
# 1. 반복문(loop)이다.
# 2. 리스트, 튜플, 세트, 딕셔너리, 문자열 등 여러 개의 요소로 구성된 "반복가능객체(iterable)"를
#    순회할 수 있다.

hobbies = ['게임', '낮잠', '넷플릭스', '골프', '영화']

print(hobbies[0])
print(hobbies[1])
print(hobbies[2])

for hobby in hobbies:
    print(hobby)

# while문으로 리스트 순회하기
# 변수 i : 리스트의 인덱스(index)를 의미한다.
i = 0
while i < 3:  # 3보다 작은 인덱스는 사용한다.
    print(hobbies[i])
    i += 1


# 일반화한 while문
# 리스트에 저장된 요소의 개수 : 리스트 길이, len() 함수
i = 0
while i < len(hobbies):  # 0 1 2 3 4
    print(hobbies[i])
    i += 1


# 연습문제.
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]
# 다음과 같이 출력하기
# 1 2 3 4 5
# 6 7 8 9 0

for five_numbers in numbers:
    # print(five_numbers)  # 없어야 함.
    for number in five_numbers:
        print(number, end=' ')  # 줄 바꿈 방지
    print()  # 줄 바꿈

# 리스트의 네이밍 추천
# 1. ~~s
# 2. ~~_list


for five_numbers in [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]:
    print(five_numbers)

# 1회 loop 동작
# for [1, 2, 3, 4, 5] in [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]:
#     print([1, 2, 3, 4, 5])
# 2회 loop 동작
# for [6, 7, 8, 9, 0] in [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]:
#     print([6, 7, 8, 9, 0])

for five_numbers in [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]:
    for number in five_numbers:
        print(number)

# 1회 loop
# for [1, 2, 3, 4, 5] in in [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]:
#     for number in [1, 2, 3, 4, 5]:
#         print(number)
# 2회 loop
# for [6, 7, 8, 9, 0] in [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]:
#     for number in [6, 7, 8, 9, 0]:
#         print(number)

print('-' * 50)

for five_numbers in numbers:
    for number in five_numbers:
        print(number, end=' ')
    print()
