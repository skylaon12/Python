# list

seasons = ['여름', '가을']
# 1. append()
# 마지막 요소로 추가
seasons.append('겨울')

# 2. insert()
# 원하는 위치에 요소 추가
seasons.insert(0, '봄')

print(seasons)

# 3. pop()
# 1) 마지막 요소를 제거
# 2) 원하는 위치의 요소를 제거
# 참고. 메소드 오버로딩
# 이름이 같은 메소드가 2개 이상 구현되어 있다.

element = seasons.pop()
print(element)  # '겨울'
print(seasons)  # ['봄' , '여름', '가을']

element = seasons.pop(0)
print(element)

print(seasons)


# set

# 1. add()
# 세트에 추가
s1 = {'제주', '속초', '가평'}
s1.add('남해')

# 2. remove()
# 제거할 대상을 지정
s1.remove('가평')

print(s1)

# 연습문제.
# lotto 번호(1 ~ 45) 6개를 입력 받아서
# lotte 세트에 저장
# 동일한 번호를 입력 하면 무시하기

lotto = {}  # 이건 dict 로 인식
lotto = set()  # 이게 set

while len(lotto) < 6:
    ball = int(input('로또번호 하나를 불러주세요 >>> '))
    if 1 <= ball <= 45:
        lotto.add(ball)

print(f'완성된 6자리 {lotto}')
