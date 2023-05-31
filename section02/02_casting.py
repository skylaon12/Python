# casting
# 1. 자료형을 바꾼다.
# 2. 문자열, 정수형, 실수형, 논리형 등 자료형의 변환을 의미한다.

# 정수형 데이터로 변경하기
# 1. 사용 함수 : int()
# 2. 변경
#    1) 실수형 : 소수점을 잘라 버린다.
#    2) 문자열 : 정수형 문자열만 가능하다. 나머지는 불가능하다.
#       '100' -> 100 (가능)
#       '1.5' -> 불가능
#    3) 논리형 : True는 1로 변환되고, False는 0으로 변환된다.
print(int(1.999))  # 1
print(int('100'))  # 100
print(int(True))   # 1
print(int(False))  # 0
# print(int('1.5'))  실행 불가

# 실수형으로 변경하기
# 1. 사용 함수 : float()
# 2. 변경
#    1) 정수형 : .0 을 추가한다.
#    2) 문자열 : 실수형 문자열만 가능하다. 나머지는 불가능하다.
#    3) 논리형 : True는 1.0으로 변환되고, False는 0.0으로 변환된다.
print(float(100))  # 100.0
print(float('1.2'))  # 1.2

# 문자열로 변경하기
# 1. 사용 함수 : str()
# 2. 모두 변경할 수 있다.
# 3. 정수나 실수의 경우 문자열의 기능이 없기 때문에 의도적으로 변경하는 경우가 있다.

# 100을 문자열로 변환하고 그 자료형을 확인해 보기
print(type(str(100)))