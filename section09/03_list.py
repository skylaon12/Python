# 1. range() 함수
# range(10)  # 0 ~ 9
# range(1, 10)  # 1 ~ 9
for n in range(10):
    print(n)

# 2. enumerate() 함수
# hobbies : ['영화', '음악', '독서']
# enumerate(hobbies)  # (0, '영화'), (1, '음악'), (2, '독서')
hobbies = ['영화', '음악', '독서']
for idx, hobby in enumerate(hobbies):
    print(idx, hobby)

# 3. sorted() 함수
scores = [6, 2, 3, 9, 1]
scores = sorted(scores)  # 오름차순 결과(0->9, 'a'->'z', '가'->'힣')를 반환
print(scores)
scores = sorted(scores, reverse=True)  # 내림차순 결과를 반환
print(scores)
