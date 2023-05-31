# 슬라이싱
# 1. 문자열의 일부를 추출하는 작업이다.
# 2. 형식
#    문자열[start:stop:step]
#    1) start : 추출에 포함되는 인덱스이다. 생략하면 처음부터 추출된다.
#    2) stop : 추출에 포함되지 않는 인덱스이다. 생략하면 끝까지 추출된다.
#    3) step : 추출할 인덱스의 차이값이다. 생략하면 1이다.
#    -- 추출범위 : start <= 추출 < stop

s = "korea"

print(s[::])  # korea
print(s[0:3])  # kor (인덱스 0부터 인덱스 3 이전까지 추출)
print(s[::2])  # kra (추출할 문자열의 인덱스 차이가 2씩 난다.)
print(s[-3:])  # rea

# 카드번호
card = '1234-5678-1212-2580'
# 1234, 5678, 1212, 2580 분리해서 출력하기
print(card[0:4])  # stop 인덱스 - start 인덱스 : 추출할 글자 수를 의미한다.
print(card[5:9])
print(card[10:14])
print(card[-4:])

print(card[0:4], card[5:9], card[10:14], card[15:19])
