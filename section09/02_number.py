# 55분 - 8시 10분

# 숫자 내장 함수

# 1. 합계, 최댓값, 최솟값
scores = [84, 96, 18, 62, 75]
print(f'합계: {sum(scores)}')
print(f'최댓값: {max(scores)}')
print(f'최솟값: {min(scores)}')

# 2. scores 평균 구하기
# 평균 = 합계 / 갯수
average = sum(scores) / len(scores)
print(f'평균: {average}')

# 3. divmod() 함수
# division + modify (몫 + 나머지)
몫, 나머지 = divmod(7, 2)
print(몫)
print(나머지)

hour, minute = divmod(150, 60)
print(hour, minute)
