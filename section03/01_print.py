# print() 함수
# 1. 출력 함수이다.
# 2. 속성
#    1) sep : 출력 대상을 연결할 문자열을 지정한다.
#    2) end : 출력 후 추가로 출력할 문자열을 지정한다.

print(2021, 7, 26)  # 출력 대상 3개를 공백으로 연결(기본값)
print(2021, 7, 26, sep=' ')  # 출력 대상 3개를 공백으로 연결
print(2021, 7, 26, sep='-')  # 2021-7-26
print(2021, 7, 26, sep=',')  # 2021,7,26  ->  csv 형식

print()  # 아무 것도 출력하지 않는다. 그리고 줄 바꾼다.
print()  # 출력 후 줄을 바꾼다. (기본값)
print()
print('hello')

# 줄을 바꾸고 싶지 않다면?
print('p', end='')  # p를 출력하고 아무 것도 출력하지 않는다.
print('i', end='')
print('e', end='')
