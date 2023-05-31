# dict
# 1. 한 데이터가 '키': '값'의 조합으로 구성된다.
# 2. '키'는 중복이 불가능하다.
# 3. '값'는 중복이 가능하다.
# 4. '값'이 데이터이고, 그 값을 찾기 위해서 '키'를 알아야 한다.
# 5. 인덱스 대신 '키'를 사용한다.

lunch = {'수': '짬뽕', '목': '제육', '금': '쌀국수'}
print(lunch['수'])
print(lunch.get('수'))

# 수요일에 짬뽕 먹었다.
# 목요일에 제육 먹었다.
# 금요일에 쌀국수 먹었다.
for key in lunch:
    print(f'{key}요일에 {lunch[key]} 먹었다.')


# 값을 빼고 싶다면? values() 메소드를 사용한다.
for value in lunch.values():
    print(value)


# 둘 다 빼고 싶다면? items() 메소드를 사용한다.
for item in lunch.items():
    print(item)
    print(f'{item[0]}요일에 {item[1]} 먹었다.')

# unpacking
for key, value in lunch.items():
    print(f'{key}요일에 {value} 먹었다.')
