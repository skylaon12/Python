# list는 저장된 요소를 변경할 수 있다.


# 1. list에 새로운 요소 추가하기
numbers = [1, 2, 3]
numbers.append(4)  # 마지막 요소로 4를 추가한다.
numbers.insert(0, 5)  # 인덱스 0에 5를 추가한다.
print(numbers)

# list에 존재하지 않는 인덱스에 값을 저장하기
# numbers[5] = 6  # IndexError 예외가 발생
# print(numbers)


# 2. list의 기존 요소 수정하기
# 수정할 요소를 불러서(인덱싱) 새로운 값을 저장한다.(덮어쓰기)
numbers[0] = 6  # 첫 번째 요소를 6으로 수정
print(numbers)

# numbers = [6, 1, 2, 3, 4]
numbers[0:2] = [100]  # 슬라이싱의 결과는 list이므로 list로 수정할 수 있다.
print(numbers)


# 3. list의 기존 요소 삭제하기
# numbers = [100, 2, 3, 4]

a = numbers.pop()  # numbers 리스트의 마지막 요소를 뺀다.(삭제된다.)
print(a)
print(numbers)

b = numbers.pop(0)  # numbers 리스트의 인덱스 0의 요소를 뺀다.
print(b)
print(numbers)

# list는 기본적으로 stack의 구조를 가지고 있다.
# append() : 마지막에 요소 추가
# pop() : 마지막의 요소 제거
