# dict
# 1. dictionary 자료형이다.
# 2. 하나의 요소가 2개의 데이터로 구성된다.
# 3. 2개의 데이터는 '키(key)'와 '값(value)'이다.
#    키(key)는 변수, 값(value)은 변수에 저장된 값으로 이해하면 좋다.

me = {
    'name': '민경태',
    'age': 44,
    'gender': '남'
}

print(me)
print(type(me))


# dict 특징
# 1. 키(key)는 중복이 불가능하다.
# 2. 값(value)은 중복이 가능하다.
# 3. 키(key)를 인덱스(index)처럼 사용할 수 있다.
print(me['name'])
print(me['age'])
print(me['gender'])

# 봄, 여름, 가을, 겨울
# spring, summer, autumn, winter
# 영한사전으로 만들어 보자.
eng_dict = {
    'spring': '봄',
    'summer': '여름',
    'autumn': '가을',
    'winter': '겨울'
}
print(eng_dict['summer'])


# dict 요소 추가
eng_dict.setdefault('snow', '눈')
eng_dict['rain'] = '비'
print(eng_dict)


# dict 요소 수정
eng_dict['spring'] = '용수철'


# dict 요소 삭제
eng_dict.pop('snow')  # 전달된 키(key)를 가진 요소 제거

print(eng_dict)

eng_dict['spring'] = ['봄', '용수철']
print(eng_dict)


# 키(key) 전체 추출
keys = eng_dict.keys()
print(keys)
print(type(keys))
print(set(keys))

# 값(value) 전체 추출
values = eng_dict.values()
print(values)
print(type(values))
print(list(values))


# (키 + 값) 전체 추출
items = eng_dict.items()
print(items)  # (키, 값)을 하나의 tuple로 추출
