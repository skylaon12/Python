# list comprehension
# 리스트 쉽게 만들기
numbers = [n for n in range(1, 11)]
print(numbers)

ten_numbers = [10 * n for n in numbers]
print(ten_numbers)

odd_numbers = [n for n in numbers if n % 2 == 1]  # 홀수
print(odd_numbers)

even_numbers = [n for n in numbers if n % 2 == 0]  # 짝수
print(even_numbers)
