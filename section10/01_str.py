# 함수 vs 메소드
# 함수 : 단독 실행한다.
# 메소드 : 누군가에 의해서(객체) 실행된다.
# print('안녕')  # print() 함수
# hobbies = []
# hobbies.append('영화')  # append() 메소드

# 문자열 함수    : 함수(문자열), 함수()
# 문자열 메소드  : 문자열.메소드()

# 1. split() 메소드
# 문자열을 분리해서 리스트로 반환
birthday = '2001 08 09'
a = birthday.split(' ')
print(a)
print(a[0], a[1], a[2])


# 2. join() 메소드
# 지정된 문자열을 이용해서 리스트의 모든 요소를 연결한 문자열을 반환
date = ['2021', '08', '09']
b = '-'.join(date)  # '2021-08-09'
print(b)
c = ''.join(date)  # '20210809'
print(c)


# 연습문제.
s = '민경태,44,남'
# split() + join() 사용으로 '민경태44남' 만들기
# s.split(',')  # ['민경태', '44', '남']
# ''.join(['민경태', '44', '남'])  # 민경태44남
s = ''.join(s.split(','))
print(s)

# 3. find() 메소드   # 문자열은 인덱싱이 가능하다.
# 지정한 문자열을 찾아서 그 인덱스를 반환
# 찾는 문자열이 다수 존재하면 첫 번째 인덱스를 반환
d = 'hello python'
idx1 = d.find('hello')  # 0
print(idx1)
idx2 = d.find('o')  # 4
print(idx2)
idx3 = d.rfind('o')  # 10 (right + find : 오른쪽에서 검색 시작)
print(idx3)

# 연습문제.  문자열 슬라이싱을 활용.
f = 'qu.es.ti.on.py'
# print(f[0:2])
dot_idx = f.rfind('.')
filename = f[:dot_idx]  # qu.es.ti.on  (처음부터 마지막 '.' 인덱스 전까지)
extname = f[dot_idx + 1:]  # py  (마지막 '.' 인덱스부터 끝까지)
print(filename)
print(extname)

# 4. replace() 메소드
# 문자열의 일부를 다른 문자열로 바꾼 결과를 반환
message = '안녕 수잔'
message = message.replace('수잔', '제시카')
print(message)
# replace() 메소드 용도
# 문자열 중 일부 문자열을 삭제하는 용도 (삭제할 문자열을 찾아서 빈문자열로 치환)
tag = '<head>'  # '<', '>' 제거
# tag.replace('<', '')  # 'head>'
# 'head>'.replace('>', '')  # 'head'
tag = tag.replace('<', '').replace('>', '')
print(tag)

# 5. 대소문자 변환
sample = 'i Am a BOY'
r1 = sample.upper()  # I AM A BOY
r2 = sample.lower()  # i am a boy
r3 = sample.capitalize()  # I am a boy
print(r1, r2, r3)

# 6. strip() 메소드
# 문자열의 앞뒤에 포함된 불필요한 문자(열) 제거
# 제거할 문자(열)을 지정할 수 있고,
# 지정 없이 공백 제거용으로 사용할 수 있다.
s = '  banana   juice  '
print(f'{s.strip()}')

# rstrip(), lstrip() 가능
# right + strip() : 오른쪽만 제거
# left + strip() : 왼쪽만 제거

s2 = '<head>'
s2 = s2.lstrip('<').rstrip('>')
print(s2)
