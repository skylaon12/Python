# set
# 1. 여러 개의 데이터를 저장할 때 사용한다.
# 2. 집합 개념(수학)의 구조이다.
# 3. 저장된 요소들 사이의 순서가 없다. (인덱스가 없다.)
# 4. 동일한 요소를 2개 이상 저장할 수 없다. (unique를 담보할 수 있다.)


# set 만들기
menus = {'떡볶이', '김밥', '순대', '김밥', '순대'}
print(menus)
print(type(menus))


# set 만들기
# set() 함수
# 1. 내용이 없는 비어 있는 set를 만들 때 사용한다.
# 2. list나 tuple을 set로 변경할 때 사용한다.
flowers = {}  # 이건 dict이다.
flowers = set()  # 이게 set이다.


hobbies = ['수영', '게임', '수영', '게임', '여행']
hobbies = set(hobbies)  # set로 변환되면서 중복이 제거된다.
hobbies = list(hobbies)
print(hobbies)

# print(list(set(hobbies)))

# hobbies = list(set(hobbies))
