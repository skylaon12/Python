# continue문
# 1. 반복문의 시작 지점으로 돌아가서 다시 시작한다.
# 2. continue문 이후의 코드는 생략된다.

# 1 ~ 9 사이만 입력을 받아서 출력한다.
# 벗어나면 재입력을 요구한다.
# 총 5개의 정수만 입력 받아서 출력한다.

# cnt = 0
# while cnt < 5:
#     number = int(input('1~9 사이 입력 >>> '))
#     if number < 1 or number > 9:
#         print('사용할 수 없습니다. 다시 입력하세요.')
#         continue  # while cnt < 5: 코드로 되돌아 간다.
#     print(f'입력 받은 값은 {number}입니다.')
#     cnt += 1


# 연습문제.
foods = ['김치', '오이', '당근', '양배추']

for food in foods:
    if food == '김치':
        continue
    else:
        print(f'{food}주스 만들자.')

for food in foods:
    if food != '김치':
        print(f'{food}주스 만들자.')


for cnt in range(5):
    number = int(input('1~9 사이 입력 >>> '))
    if number < 1 or number > 9:
        print('사용할 수 없습니다. 다시 입력하세요')
        continue  # 이건 불가하다.
    print(f'입력 받은 값은 {number}입니다.')


