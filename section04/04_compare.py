# 비교 연산
# 1. >, >=, <, <=, ==(equal), !=(not equal)
# 2. 결과는 bool이다. (True, False)

a, b = 7, 2

print(a > b)  # True
print(a >= b)
print(a < b)  # False
print(a <= b)
print(a == b)
print(a != b)

# 파이썬은 사이값 비교가 가능하다.
print(1 <= a <= 10)  # True


# 참고.
# 다른 언어들은 1 <= a <= 10을 이렇게 해석한다.
# 먼저 1 <= a 만 처리한다. 결과는 True 이다.
# 그 다음으로 True <= 10 를 처리한다. True 는 1 이므로 최종 True 이다.
# a 의 값과 상관 없이 항상 True 이다.


# in
# 포함 여부를 확인한다.

s = 'python'
print('a' in s)  # 'a'가 s에 포함되어 있으면 True, 아니면 False

cart = ['두부', '계란', '생선', '삼겹살', '우유']
print('김치' in cart)
print('계란' in cart)


# 연습문제.
lotto = [34, 44, 1, 20, 18, 36]  # 이게 안 보인다고 생각하고,

# 1~45 사이 정수를 하나만 입력 받아서,
# 있는지 없는지 출력하기

pick = int(input('입력 >>> '))
print(pick in lotto)
