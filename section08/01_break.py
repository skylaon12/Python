# break문
# 1. 반복문(while, for)을 종료한다.
# 2. 무한 루프와 함께 사용되는 경우가 많다.

number = 1
while True:
    number += 2
    if number == 99:
        break

print(number)

# 연습문제.
# 사용자가 1 ~ 9 사이의 값을 입력한다.
# 1. 1 ~ 9 범위를 벗어난 입력은 무시하고 다시 입력 받는다.
# 2. 사용자가 7을 입력하면 그만 입력 받는다.

# while True:
#     number = int(input('1~9사이를 입력하세요 >>> '))
#     if number == 7:
#         break
#
# print('나왔다')

# 연습문제.
# 5x5=25 출력이 끝나면 그만 출력한다.
stop = False  # 계속 하는 경우 False, 그만 두는 경우 True
for dan in range(2, 10):
    for n in range(1, 10):
        print(f'{dan}x{n}={dan * n}')
        if dan == 5 and n == 5:
            stop = True
            break
    if stop:  # if stop == True:
        break

stop = False
for n in range(1, 10):
    for dan in range(2, 10):
        print(f'{dan}x{n}={dan * n}', end='\t')
        stop = (dan == 5 and n == 5)
        if stop:
            break
    if stop:
        break
    print()
