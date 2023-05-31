# tuple
# 1. 여러 값을 저장할 때 사용한다.
# 2. 저장된 값을 변경(추가, 수정, 삭제)이 불가능하다.
# 3. 소괄호()로 묶어서 표현한다.


# tuple 만들기
seasons = ('봄', '여름', '가을', '겨울')
print(seasons)
print(type(seasons))


# tuple 만들기 주의사항
# 하나의 요소만 저장하는 경우
# 마지막에 반드시 콤마(,)를 추가해야 한다.
t = ('민경태',)
print(t)
print(type(t))


# tuple 만들기
# packing : 여러 값을 동시에 저장하면 tuple에 저장된다.
me = '민경태', 44, '남', ['서울', '02-123-4567']
print(me)
print(type(me))


# tuple 만들기
# tuple() 함수
# 다른 자료형을 tuple로 변환
you = tuple(['브레드', 50])
print(you)


# packing의 반대 과정
# unpacking : 튜플의 요소를 여러 변수에 나눠서 저장
name, age = you
print(name, age)


# tuple은 indexing, slicing 모두 지원한다.
# you = ('브레드', 50)
print(you[0])  # 브레드
print(you[0][0])  # 브
print(you[0][1])  # 레
print(you[0][2])  # 드
print(you[1])  # 50


# tuple() 함수 : tuple로 변환
# list() 함수 : list로 변환

weeks = ('일', '월')
weeks = list(weeks)  # tuple인 weeks를 list로 바꿔서 덮어쓰기를 한다.
weeks.append('화')
weeks.append('수')
weeks.append('목')
weeks.append('금')
weeks.append('토')
weeks = tuple(weeks)  # list인 weeks를 tuple로 바꿔서 덮어쓰기를 한다.
print(weeks)
