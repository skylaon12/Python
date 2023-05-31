# range() 함수
# 1. 범위를 만드는 함수이다.
# 2. 슬라이싱과 유사하다.
# 3. 형식
#    range(start, stop, step)
#    start <= 범위 < stop
#    1) start : 생략 가능, 생략하면 0
#    2) stop  : 생략 불가능
#    3) step  : 생략 가능, 생략하면 1씩 증가

# range(5) : 0부터 4까지 생성
print(range(5))
print(list(range(5)))

# for문에서는 range(5)와 list(range(5))의 차이는 없다.
for number in range(5):
    print(number)


hobbies = ['음악', '영화', '독서']
for i in range(len(hobbies)):  # i는 0, 1, 2 즉 인덱스를 의미한다.
    print(f'인덱스:{i}, 요소:{hobbies[i]}')


# range() 함수를 이용하면 원하는 loop 횟수를 쉽게 만들 수 있다.
for n in range(3):
    print('만세')

for _ in range(3):
    print('만세')


# 연습문제.
# 2단만 구구단 출력하기
for n in range(1, 10):  # n : 1 ~ 9
    print(f'2x{n}={2 * n}')

# 전체 구구단 출력하기
for dan in range(2, 10):  # dan : 2 ~ 9
    for n in range(1, 10):
        print(f'{dan}x{n}={dan * n}')
# dan = 2, n = 1
# dan = 2, n = 2
# dan = 2, n = 3
# ...
# dan = 2, n = 9
# dan = 3, n = 1
# ...

# 전체 구구단 출력하기.
# 2x1=2  3x1=3  4x1=4  ... 9x1=9
# 2x2=4  3x2=6  4x2=8  ... 9x2=18
# ...
# 2x9=18 3x9=27 4x9=36 ... 9x9=81

# for dan in range(2, 10):
#     print(f'{dan}x1={dan * 1}', end='\t')
# print()
#
# for dan in range(2, 10):
#     print(f'{dan}x2={dan * 2}', end='\t')
# print()
#
# for dan in range(2, 10):
#     print(f'{dan}x3={dan * 3}', end='\t')
# print()

for n in range(1, 10):
    for dan in range(2, 10):
        print(f'{dan}x{n}={dan * n}', end='\t')
    print()
