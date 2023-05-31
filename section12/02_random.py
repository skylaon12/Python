# random 모듈
# 표준 모듈
# 난수를 생성한다.


# import random
import random as rd  # random 모듈의 별명(alias)을 rd 로 지정한다. (random 대신 rd 를 사용)

# 실수형 난수 생성
print(rd.random())  # 0.0 <= 난수 < 1.0

# 실수형 난수 범위
# 0.0 <= 난수 < 1.0 범위는 백분율 범위로 보는 것이 타당하다.
#  0% <= 난수 < 100%

# 실수형 난수는 확률 처리용으로 사용한다.

# 5% 확률로 '강화 성공', 나머지 확률로 '강화 실패' 출력하기.
if rd.random() < 0.05:
    print('강화 성공')
else:
    print('강화 실패')


# 정수형 난수
print(rd.randint(1, 10))  # 1 <= 난수 <= 10


# 6자리 인증코드 생성하기
def create_auth_code():

    auth_code = ''

    for _ in range(6):  # 6번의 반복을 실행
        auth_code = auth_code + str(rd.randint(0, 9))  # auth_code += str(rd.randint(0, 9))

    return auth_code


print(create_auth_code())


# 연습문제.
# 1 ~ 5 중 하나를 생성한다.
# 4 이상이면 한 번 더 생성한다.

names = ['', '도', '개', '걸', '윷', '모']


def throw_yut():
    yut = rd.randint(1, 5)
    print(f'{names[yut]}, {yut}칸 이동')
    if yut >= 4:
        throw_yut()


throw_yut()


# 단판 가위바위보
# 1. 숫자로 가위바위보를 한다.
# 2. 가위는 1, 바위는 2, 보는 3으로 한다.
# 3. 컴퓨터 : 1, 2, 3 중 하나를 랜덤 생성한다.
# 4. 사용자 : 1, 2, 3 중 하나를 입력한다.
# 5. 실행 예시
#    넌 가위를 냈고, 컴퓨터는 바위를 냈어. 넌 졌다.

def play_srp():
    srp = ['', '가위', '바위', '보']
    com = rd.randint(1, 3)
    user = int(input('가위는 1, 바위는 2, 보는 3 >>> '))
    print(f'넌 {srp[user]}를 냈고, 컴퓨터는 {srp[com]}를 냈어. 넌 ', end='')
    diff = user - com
    if diff == 0:
        print('비겼다.')
    elif diff == -2 or diff == 1:
        print('이겼다.')
    else:
        print('졌다.')


play_srp()
