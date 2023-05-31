# input() 함수
# 1. 입력 함수이다.
# 2. 사용자가 어떤 값을 입력할 수 있다.
# 3. 화면 하단의 실행 창을 통해서 입력한다.
# 4. 입력 받은 값을 저장할 변수가 반드시 필요하다.
# 5. 입력 받은 값은 언제나 str 자료형이다.


# a = input()
# print('입력한값', a, sep=':')
# print('입력자료형', type(a), sep=':')


# name = input('이름을 입력하세요 >>> ')
# print('입력된 이름은', name, '입니다.')


# int('50') : 50

# age = input('나이를 입력하세요 >>> ')
# print('내년 나이는', (int(age) + 1), '살입니다.')

# age = int(input('나이를 입력하세요 >>> '))
# print('내년 나이는', age + 1, '살입니다.')


# float('1.5') : 1.5

# weight = float(input('몸무게를 입력하세요 >>> '))
# print('내년 목표 몸무게는', (weight - 1), 'kg입니다.')


# 연습문제.
# 0~100 사이의 국어, 영어, 수학 (모두 정수형) 점수를 입력 받아서
# 평균을 출력한다.

# kor = int(input('국어>>>'))
# eng = int(input('영어>>>'))
# mat = int(input('수학>>>'))

# kor, eng, mat = int(input('국어>>>')), int(input('영어>>>')), int(input('수학>>>'))
# ave = (kor + eng + mat) / 3

# 반올림 처리한다면,
# ave = round(ave, 2)
#
# print('평균점수는', ave, '점입니다.')

# 혹시 리스트를 사용하신 분?
# s = []
# s.append(int(input('국어>>>')))
# s.append(int(input('영어>>>')))
# s.append(int(input('수학>>>')))

# 리스트는 합계를 구하는 메소드가 있다.
# ave = round(sum(s) / 3, 2)
# print('평균점수는', ave, '점입니다.')


# 연습문제
# 간단 윷놀이 : 도/개/걸/윷/모 중 하나를 입력 받아서 아래와 같이 출력한다.
# 입력 >>> 걸
# 걸은 3칸 움직인다.
yut = {
    '도': 1,
    '개': 2,
    '걸': 3,
    '윷': 4,
    '모': 5
}

# print(yut['도'])  # 1
# print(yut.get('도'))  # 1
a = input('입력 >>> ')
print(a, '는', yut[a], '칸 움직인다.')
