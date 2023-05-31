score = int(input('점수를 입력하세요 >>> '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print('점수는 {}점이고, 학점은 {}학점입니다.'.format(score, grade))
