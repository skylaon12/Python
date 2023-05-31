# 조건 연산
# 1. 조건은 비교 연산으로 만든다.
# 2. 비교 연산의 결과가 True 일 때와 False 일 때 모두 처리한다.

age = int(input('나이? >>> '))
print('성인' if age >= 20 else '미성년자')
print(f'입력된 {age}살은 나이가 {"아니다" if age < 0 or age > 120 else "맞다"}.')

# 0 ~ 7 : 미취학아동
# 8 ~ 19 : 초중고생
# 20 ~ 120 : 성인
print('미취학아동' if 0 <= age <= 7 else '초중고생' if 8 <= age <= 19 else '성인' if 20 <= age <= 120 else '알 수 없음')


# 연습문제.
# 어떤 정수를 하나 입력 받아서 짝수/홀수 구분해서 출력하기.
# 홀수(odd number) : 2로 나눈 나머지(%)가 1인 수
# 짝수(even number) : 2로 나눈 나머지(%)가 0인 수

# 5의 배수 여부 출력하기.
# 5의 배수 : 5로 나눈 나머지(%)가 0인 수

n = int(input('정수 입력 >>> '))
print('짝수' if n % 2 == 0 else '홀수')
print('홀수' if n % 2 == 1 else '짝수' if n % 2 == 0 else '')

print('5의 배수' if n % 5 == 0 else '5의 배수 아님')

print('5의 배수' if n % 5 == 0 else '짝수' if n % 2 == 0 else '홀수')
