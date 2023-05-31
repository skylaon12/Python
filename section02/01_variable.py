# 주석 comment
'''
주석
여러 줄의 설명이 필요할 때
사용합니다.
'''

# 파이썬 코드 작성
# 1. 대문자와 소문자를 구분한다.
# 2. 가급적 소문자를 사용하고, 목적이 있는 경우 대문자를 사용한다.
# 3. 한글도 가능하지만 가능하면 사용하지 않는다.
# 4. 기본 작명 규칙(naming convension)은 snake case(밑줄로 각 단어를 연결하는 방식)이다.

# 참고. 작명 규칙의 종류
# 1. snake case : my_name
# 2. lower camel case : myName
# 3. upper camel case : MyName

# 변수
# 1. 어떤 데이터를 저장하는 장소
# 2. 변수 생성 방법
#    변수명 = 값
# 3. 동적 타이핑(동적 자료형)을 지원한다.
#    변수는 저장되는 값의 자료형에 따라서 알아서 세팅된다.

# 정적 타이팅(정적 자료형)
# int my_age;  # 사용 이전에 미리 자료형을 정해둔다.
# my_age = 44;  성공
# my_age = '민경태';  실패

my_name = '민경태'
my_gender = "남자"
my_age = 44
my_eye = 1.2
is_adult = True

# 데이터 표현 방법 (literal, 리터럴)
# 1. 문자열(str) : 작은 따옴표 또는 큰 따옴표로 묶는다.
# 2. 정수형(int) : 그냥 입력한다.
# 3. 실수형(float) : 그냥 입력한다.
# 4. 논리형(bool) : 참을 의미하는 True, 거짓을 의미하는 False

# 데이터 확인
print(my_name)
print(my_gender)
print(my_age)
print(my_eye)
print(is_adult)

# 변수의 자료형(type) 확인
# type() 함수 : 변수의 자료형을 반환한다.
print(type(my_name))  # str (string)
print(type(my_gender))  # str
print(type(my_age))  # int (integer)
print(type(my_eye))  # float (floating point)
print(type(is_adult))  # bool (boolean)

# 한 번 결정된 자료형을 바꿀 수 있는가? Yes
my_age = 44.5
print(type(my_age))
