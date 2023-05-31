# function
# 1. 내장 함수(builtin)와 사용자 함수(user)로 구분한다.
# 2. 함수 단위로 코드를 관리한다.
#    - 나누어 정복하라. (Divide and Conquer)
# 3. 하나의 함수는 하나의 기능을 포함하는 것이 좋다.

# 사용자 함수(user define)
# 1. 함수를 만든다. (함수 정의)
# 2. 함수를 사용한다. (함수 호출)

# 함수 정의
# def 함수명(매개변수):
#     함수본문
#     return 반환값(결과값)

# 함수 호출
# 함수명(인수)


# 내가 만든 my_print()

# 특수문자 : 자음(ㄱ, ㄴ, ㄷ, ) + 한자 키

# 함수 정의
def my_print(content):  # 매개변수 content : 전달된 인수를 보관
    print(f'★{content}★')


# 함수 호출
my_print('안녕하세요')  # 인수 : my_print() 함수로 전달하는 '안녕하세요'
my_print('반갑습니다')


# 객체 ?
# 일반 : 값 + 기능
# 파이썬 : 모든 변수는 사실 객체이다.

# 함수 정의
def what_time(hour, minute, second):
    print(f'{hour}시 {minute}분 {second}초')


# 함수 호출
what_time(20, 11, 30)  # 20시 11분 30초


# 함수는 반드시 먼저 만들고, 나중에 호출한다.
def hi():
    print('안녕하세요')


hi()
hi()
hi()
