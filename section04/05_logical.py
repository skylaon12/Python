# 논리 연산
# 1. and : 모든 비교가 True 이면 True, 아니면 False
# 2. or  : 모든 비교 중 하나라도 True 이면 True, 아니면 False
# 3. not : 비교 결과를 반대로 변경


# 참고.
# 1 <= a <= 10 사이 비교는 대부분 아래와 같이 처리한다.
a = 55
print(a >= 1 and a <= 10)


# 나이를 입력 받아서 정상인지 점검
age = int(input('몇 살이노?'))
print(age < 0 or age > 120)  # 0~120 범위를 벗어나면 True


# 너 미성년자지?  직접 비교할 것.
# 너 성인 아니지?  반대로 꼬지말 것.
print(not age >= 20)  # 미성년자이면 True
