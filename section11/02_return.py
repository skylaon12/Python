# 반환이 있는 함수


# 1을 전달하면, '안녕하세요'
# 2를 전달하면, 'hello'
# 나머지는 '봉주르'

def hi(n):
    if n == 1:
        return '안녕하세요'  # hi() 호출한 곳으로 되돌려 주는 값
    elif n == 2:
        return 'hello'
    else:
        return '봉주르'


a = hi(3)
print(a)

print(hi(1))


# 다음 시간을 반환
# 1을 전달하면 2를 반환
# 2를 전달하면 3을 반환
# 12를 전달하면 1을 반환

def next_time(hour):
    if hour == 12:
        return 1
    else:
        return hour + 1


h = 12
print(f'{h}시 다음 시간은 {next_time(h)}시이다.')
# 1시 다음 시간은 2시이다.


# return 은 함수를 종료하는 용도로도 사용한다.

def piggy(money):
    if money <= 0:
        print(f'{money}원은 저금할 수 없습니다.')
        return  # 반환 값이 없는 return 은 함수의 종료를 의미한다.
    print(f'{money}원 저금되었습니다.')


# def piggy(money):
#     if money > 0:
#         print(f'{money}원 저금되었습니다.')
#     else:
#         print(f'{money}원은 저금할 수 없습니다.')


piggy(1000)
piggy(-2000)  # 실행되지 않도록!


# 1. 인수-매개변수
#    디폴트 매개변수
#    가변 매개변수

# 2. 반환
#    다중 반환
