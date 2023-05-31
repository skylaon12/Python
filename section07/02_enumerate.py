# enumerate() 함수
# 1. 리스트의 인덱스와 요소를 동시에 반환한다.
# 2. 인덱스와 요소를 튜플로 반환한다.


hobbies = ['헬스', '야식', '낮잠']

for t in enumerate(hobbies):
    print(t)


# 튜플. 간단 리뷰
# 튜플은 packing과 unpacking이 가능하다.
me = '민경태', 44  # packing, me는 튜플이다.
print(me)
name, age = me  # unpacking
print(name, age)

for i, hobby in enumerate(hobbies):
    print(f'인덱스: {i}, 요소: {hobby}')

# enumerate() 함수를 모르면,,,
for i in list(range(len(hobbies))):
    print(f'인덱스: {i}, 요소: {hobbies[i]}')


# 리뷰. 리스트 요소 삭제
you = ['민경태', 44, 177.5]
you.pop(2)
print(you)


# 연습문제.
# 꽃 이름이 4글자 이상이면 리스트에서 제거한다.
flowers = ['장미', '코스모스', '튤립', '프리지아', '안개']
targets = []

for i, flower in enumerate(flowers):
    print(f'인덱스{i}의 꽃은 {flower}입니다.')
    if len(flower) >= 4:
        print(f'{flower} 지웁니다.')
        targets.append(i)  # flowers.pop(i)

for i in sorted(targets, reverse=True):  # targets : [1, 3], sorted(targets, reverse=True) : [3, 1], 내림차순으로 정렬하기
    flowers.pop(i)

print(f'남은 꽃들은 {flowers}입니다.')


# [ a, b, c ] : 1회 순회시 인덱스 0 접근, a 사용
# [ a, b, c ] : 2회 순회시 인덱스 1 접근, b 사용
# [ a, b, c ] : 3회 순회시 인덱스 2 접근, c 사용

# [ a, b, c ] : 1회 순회시 인덱스 0 접근, a 사용, a 삭제
# [ b, c ]    : 2회 순회시 인덱스 1 접근, c 사용
# [ b, c ]    : 3회 순회시 인덱스 2 접근, 인덱스 오류
