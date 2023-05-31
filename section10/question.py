# 잘 푸셨습니다~~
# practice8-3.py
password = 'qwerty'
for n in range(1, 6):
    guess = input(f'비밀번호를 입력하세요({5 - n}번 남음) >>> ')
    if guess == password:
        print(f'{n}번만에 비밀번호를 맞혔습니다.')
        break
    if n == 5:
        print('비밀번호 입력 횟수를 초과했습니다.')
