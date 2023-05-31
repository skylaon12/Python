# str 기본 특징
# 1. 작은 따옴표('), 큰 따옴표(") 모두 사용할 수 있다.
#    따옴표를 포함하는 문자열 처리에 탁월하다.
#    예시 : '{"name": "민경태"}'
# 2. 삼중 따옴표(''' 또는 """)는 사실 주석 처리용이 아니다.
#    여러 줄의 문자열을 묶는 경우에 사용한다.
# 3. 이스케이프 문자를 지원한다.(특수문자 지원)
#    엔터, 탭, 따옴표 등
#    1) 엔터 : \n  (시스템에 따라서 \n\r)
#    2) 탭 : \t
#    3) 따옴표 : \'  또는  \"

data1 = '{"name": "민경태"}'  # 파이썬, 자바스크립트 등
data2 = "{\"name\": \"민경태\"}"  # C계열, 자바 등

print(data1)
print(data2)

address1 = '''우편번호 12345
서울시 마포구 서강로
아이비타워 3층'''
address2 = '우편번호 12345\n서울시 마포구 서강로\n아이비타워 3층'

print(address1)
print(address2)


# 인덱싱
# 1. 문자열의 글자마다 부여된 번호를 의미한다.
# 2. 앞에서부터 시작하면 0부터 시작이다.
# 3. 뒤에서부터 시작하면 -1부터 시작이다.

city = 'seoul'

# 유사한 코드는 ctrl + d 로 복제하면 편리하다.
print(city[0])  # s
print(city[1])  # e
print(city[2])  # o
print(city[3])  # u
print(city[4])  # l

print(city[-1])  # l
print(city[-2])  # u
print(city[-4])  # e
print(city[-3])  # o
print(city[-5])  # s

# str(100) -> '100'
# type(str(100)) -> type('100') -> str

# print(str(15)[-1])
