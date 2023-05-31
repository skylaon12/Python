# if문만 나열하면 좋지 않다.
# 언제나 if문의 개수만큼 비교 연산을 수행한다.
score = 85
if 90 <= score <= 100:
    grade = 'A'
if 80 <= score < 90:
    grade = 'B'
if 70 <= score < 80:
    grade = 'C'
if 0 <= score < 70:
    grade = 'D'
print(f'점수 {score}점, 등급 {grade}')


if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score:  # elif == else + if 합성어
    grade = 'B'
elif 70 <= score:
    grade = 'C'
elif 0 <= score:
    grade = 'D'
print(f'점수 {score}점, 등급 {grade}')


if score < 0 or score > 100:
    grade = '없는 등급'
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'
print(f'점수 {score}점, 등급 {grade}')


# 연습문제.

# 체질량지수(BMI) = 몸무게(kg) / 키(m)의 제곱

# 체질량지수
# 저체중 : 18.5 미만
# 정상   : 18.5 이상 23 미만
# 과제중 : 23 이상 25 미만
# 비만   : 25 이상

weight = float(input('몸무게(kg)를 입력하세요 >>> '))
height = float(input('키(cm)를 입력하세요 >>> '))

height /= 100  # height = height / 100  단위 cm -> 단위 m

# bmi = weight / (height * height)  아래 코드와 동일하다.

# bmi = weight / (height ** 2)

bmi = round(weight / (height ** 2), 2)  # 소수 2자리로 반올림

if bmi < 18.5:
    health = '저체중'
elif bmi < 23:
    health = '정상'
elif bmi < 25:
    health = '과체중'
else:
    height = '비만'

print(f'체질량지수: {bmi}, 건강상태: {health}')
