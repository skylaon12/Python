# 문자열 관련 내장 함수

# 1. str() 함수
a = str(100)
b = str(1.5)
print(a + b)  # 1001.5

# 2. eval() 함수
# 강력하지만 보안 이슈가 있다. 사용은 자제.
total = '1 + 2'
print(total)
print(eval(total))  # eval() 함수에 전달한(문자열 전달) 파이썬 코드를 실행한다.

# 3. format() 함수
n = format(1000000, ',')
print(n)
